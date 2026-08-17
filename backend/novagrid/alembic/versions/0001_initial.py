from alembic import op
import sqlalchemy as sa

revision="0001_initial"
down_revision=None
branch_labels=None
depends_on=None

def upgrade():
    op.create_table("api_sources",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("name",sa.String(255),nullable=False),sa.Column("spec_url",sa.Text()),sa.Column("spec_path",sa.Text()),sa.Column("repo_path",sa.Text()),sa.Column("last_hash",sa.String(64)),sa.Column("active",sa.Boolean(),nullable=False,server_default=sa.true()),sa.Column("created_at",sa.DateTime(),nullable=False))
    op.create_table("api_versions",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("source_id",sa.Integer(),sa.ForeignKey("api_sources.id",ondelete="CASCADE"),nullable=False),sa.Column("version_number",sa.Integer(),nullable=False),sa.Column("spec_hash",sa.String(64),nullable=False),sa.Column("spec_json",sa.JSON(),nullable=False),sa.Column("created_at",sa.DateTime(),nullable=False))
    op.create_table("api_changes",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("source_id",sa.Integer(),sa.ForeignKey("api_sources.id",ondelete="CASCADE"),nullable=False),sa.Column("from_version_id",sa.Integer(),sa.ForeignKey("api_versions.id"),nullable=False),sa.Column("to_version_id",sa.Integer(),sa.ForeignKey("api_versions.id"),nullable=False),sa.Column("classification",sa.String(50),nullable=False),sa.Column("summary",sa.Text(),nullable=False),sa.Column("changes_json",sa.JSON(),nullable=False),sa.Column("created_at",sa.DateTime(),nullable=False))
    op.create_table("dependencies",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("source_id",sa.Integer(),sa.ForeignKey("api_sources.id",ondelete="CASCADE"),nullable=False),sa.Column("affected_service",sa.String(255),nullable=False),sa.Column("file_path",sa.Text(),nullable=False),sa.Column("symbol",sa.String(255)),sa.Column("method",sa.String(20),nullable=False),sa.Column("path_pattern",sa.Text(),nullable=False),sa.Column("created_at",sa.DateTime(),nullable=False))
    op.create_table("impact_reports",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("change_id",sa.Integer(),sa.ForeignKey("api_changes.id",ondelete="CASCADE"),nullable=False),sa.Column("affected_service",sa.String(255),nullable=False),sa.Column("file_path",sa.Text(),nullable=False),sa.Column("impact_level",sa.String(50),nullable=False),sa.Column("explanation",sa.Text(),nullable=False),sa.Column("recommendation",sa.Text(),nullable=False),sa.Column("status",sa.String(50),nullable=False,server_default="OPEN"),sa.Column("created_at",sa.DateTime(),nullable=False))
    op.create_table("fixes",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("change_id",sa.Integer(),sa.ForeignKey("api_changes.id",ondelete="CASCADE"),nullable=False),sa.Column("description",sa.Text(),nullable=False),sa.Column("patch",sa.Text()),sa.Column("status",sa.String(50),nullable=False,server_default="PROPOSED"),sa.Column("created_at",sa.DateTime(),nullable=False))
    op.create_table("test_runs",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("change_id",sa.Integer(),sa.ForeignKey("api_changes.id",ondelete="CASCADE"),nullable=False),sa.Column("passed",sa.Boolean(),nullable=False),sa.Column("exit_code",sa.Integer(),nullable=False),sa.Column("output",sa.Text(),nullable=False),sa.Column("duration_seconds",sa.Float(),nullable=False),sa.Column("created_at",sa.DateTime(),nullable=False))

def downgrade():
    for table in ["test_runs","fixes","impact_reports","dependencies","api_changes","api_versions","api_sources"]:
        op.drop_table(table)
