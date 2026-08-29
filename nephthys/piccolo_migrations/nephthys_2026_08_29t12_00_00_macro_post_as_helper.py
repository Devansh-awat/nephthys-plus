from nephthys.database.raw_migration import raw_migration

ID = "2026-08-29T12:00:00:000000"
VERSION = "1.33.0"
DESCRIPTION = "Add postAsHelper column to Macro"


async def forwards():
    return raw_migration(
        migration_id=ID,
        app_name="nephthys",
        description=DESCRIPTION,
        forwards="""
ALTER TABLE "Macro" ADD COLUMN "postAsHelper" BOOLEAN NOT NULL DEFAULT false;
""",
        backwards="""
ALTER TABLE "Macro" DROP COLUMN IF EXISTS "postAsHelper";
""",
    )
