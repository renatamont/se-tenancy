# STANDARD IMPORTS
import logging

# PROJECT IMPORTS
from src.infrastructure.db_config.db import PostgresDBInfrastructure


class SqlAlchemyRepositories:
    infra = PostgresDBInfrastructure

    @classmethod
    async def get_courses_by_class_id(cls, tenant, class_id):

        session = cls.infra.get_session(schema=tenant)

        try:
            query = f"""
                    SELECT course_id 
                    FROM {tenant}.portal_classcourse
                    WHERE class_school_id = {class_id}
                    """
            result = session.execute(query).fetchall()

            return result
        except Exception as e:
            logging.error(f"Error executing query: {e}")
            raise
        finally:
            session.close()
