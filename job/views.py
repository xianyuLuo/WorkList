from job.serializers import LevelSerializer, JobSerializer
from job.models import level, job
from rest_framework import generics

class LevelList(generics.ListAPIView):
    """
    get:
    # 返回LevelList
    ## 可选参数
    ### id
    ```
    levelid，如 1 2 3
    ```

    ### level_name
    ```
    level名称，如“重要不紧急”
    ```
    """
    queryset = level.objects.all()
    serializer_class = LevelSerializer

    def get_queryset(self):
        queryset = level.objects.all()
        id = self.request.query_params.get('id')
        level_name = self.request.query_params.get('level_name')
        if id:
            queryset = queryset.filter(id = id)
        if level_name:
            queryset = queryset.filter(level_name = level_name)
        return queryset

class JobList(generics.ListCreateAPIView):
    """
    get:
    # 返回job列表
    ## 可过滤参数
    ### job_level
    ```
    level的id，获取方式见 levellist
    ```

    ### job_date
    ```
    时间，如 2018-11-2
    ```

    ### job_isover
    ```
    job是否完成，True / False
    ```

    ## 使用样例
    ```
    curl http://127.0.0.1:8000/joblist/?level_id=2&job_date=2018-11-2&job_isover=false
    ```

    post:
    # 新增job
    ## 必选参数
    ### job_level
    ```
    level的id，获取方式见 levellist
    ```

    ### job_date
    ```
    时间，如 2018-11-2
    ```

    ### job_isover
    ```
    job是否完成，True / False
    ```

    ### job_content
    ```
    job详情
    ```

    ## 可选参数
    ### job_comment
    ```
    job备注
    ```
    """
    queryset = job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = job.objects.all()
        job_level = self.request.query_params.get('job_level')
        job_date = self.request.query_params.get('job_date')
        job_isover = self.request.query_params.get('job_isover')
        if job_level:
             queryset = queryset.filter(job_level_id = job_level)
        if job_date:
            queryset = queryset.filter(job_date = job_date)
        if job_isover:
            queryset = queryset.filter(job_isover = job_isover)
        return queryset