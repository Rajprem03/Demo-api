import json

from scanner.repository import scan_repository
from scanner.detector import detect_api_calls


PROJECT_PATH = "./test_project"
OUTPUT_FILE = "reports/scan_results.json"


def main():

    print("\n")
    print("=" * 70)
    print("                 NOVAGRID API SCANNER")
    print("=" * 70)

    files = scan_repository(PROJECT_PATH)

    print(f"\n📁 Files scanned: {len(files)}")

    all_apis = []

    for file in files:

        try:
            code = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )
        except Exception:
            continue

        api_calls = detect_api_calls(code)

        for api in api_calls:

            api_result = {
                "file": str(file),
                "line": api["line"],
                "method": api["method"],
                "url": api["url"],
                "type": api["type"],
                "parameters": api["parameters"],
                "body": api["body"]
            }

            all_apis.append(api_result)

            print("\n" + "-" * 70)
            print("🌐 API DEPENDENCY")
            print("-" * 70)

            print(f"📄 File       : {file}")
            print(f"📍 Line       : {api['line']}")
            print(f"🔧 Method     : {api['method']}")
            print(f"🔗 URL        : {api['url']}")
            print(f"📦 Type       : {api['type']}")

            if api["parameters"]:

                print("\n🔹 Parameters:")

                for parameter in api["parameters"]:
                    print(f"   • {parameter}")

            if api["body"]:

                print("\n📦 Request Body:")

                for field in api["body"]:
                    print(f"   • {field}")

    # ---------------------------------------------
    # Save JSON report
    # ---------------------------------------------

    report = {
        "total_files": len(files),
        "total_apis": len(all_apis),
        "apis": all_apis
    }

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as output:

        json.dump(
            report,
            output,
            indent=4
        )

    print("\n" + "=" * 70)
    print(f"🌐 Total API calls found: {len(all_apis)}")
    print("=" * 70)

    print(f"\n💾 Scan report saved to: {OUTPUT_FILE}")

    print("\n✅ NovaGrid scan completed successfully!\n")


if __name__ == "__main__":
    main()