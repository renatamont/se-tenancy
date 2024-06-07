# STANDARD IMPORTS
from fastapi import FastAPI, Response, Request
from starlette import status
import json

# PROJECT IMPORTS
from src.routers.reports.router import CourseReportRouter
from src.domain.exceptions.exceptions import (
    InternalServerError,
    BadRequestError,
    ForbiddenError,
    UnauthorizedError,
    ErrorFetchingData,
    InvalidParams
)


class BaseRouter:

    app = FastAPI(
        title="ISIS API",
        description="Micro-service able to accept RESTFUL requests connecting with ",
    )

    @staticmethod
    def __register_router_course_report():
        report_router = CourseReportRouter.get_course_report_router()
        BaseRouter.app.include_router(report_router)
        return BaseRouter.app

    @staticmethod
    def register_routers():
        BaseRouter.__register_router_course_report()

        return BaseRouter.app

    @staticmethod
    @app.middleware("http")
    async def middleware_response(request: Request, call_next: callable):
        middleware_service_response = await BaseRouter.__add_process_time_header(
            request=request, call_next=call_next
        )
        return middleware_service_response

    @staticmethod
    async def __add_process_time_header(request: Request, call_next):
        try:
            response = await call_next(request)

        except UnauthorizedError as e:
            return Response(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content=json.dumps(
                    {"request_status": False, "status": 1, "msg": e.args[0]}
                ),
            )

        except ErrorFetchingData as e:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=json.dumps(
                    {"request_status": False, "status": 2, "msg": e.args[0]}
                ),
            )

        except InvalidParams as e:
            return Response(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                content=json.dumps(
                    {"request_status": False, "status": 9, "msg": e.args[0]}
                ),
            )

        except ForbiddenError as e:
            return Response(
                status_code=status.HTTP_403_FORBIDDEN,
                content=json.dumps(
                    {"request_status": False, "status": 5, "msg": e.args[0]}
                ),
            )

        except BadRequestError as e:
            return Response(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=json.dumps(
                    {"request_status": False, "status": 6, "msg": e.args[0]}
                ),
            )
        except InternalServerError as e:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=json.dumps(
                    {"request_status": False, "status": 7, "msg": e.args[0]}
                ),
            )

        except Exception as e:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=json.dumps(
                    {
                        "request_status": False,
                        "status": 8,
                        "msg": f"An unexpected error occurred, {e}",
                    }
                ),
            )

        return response
