### Request Address

/v2/sops/get_template_list/

### Request Method

GET

### Functional description

Query flow templates list of the business

### Request Parameters

#### General Parameters

|   Field         |  Type       | Required |  Description    |
|-----------------|-------------|---------|------------------|
|   bk_app_code   |   string    |   YES    |  APP ID |
|   bk_app_secret |   string    |   YES    |  APP Secret(APP TOKEN), which can be got via BlueKing Developer Center -> Click APP ID -> Basic Info |
|   bk_token      |   string    |   NO     |  Current user login token, bk_token or bk_username must be valid, bk_token can be got by Cookie      |
|   bk_username   |   string    |   NO     |  Current user username, APP in the white list, can use this field to specify the current user        |

#### Interface Parameters

| Field          |  Type       | Required   |  Description             |
|---------------|------------|--------|-------------------|
| bk_biz_id     |  string    | YES     | the business ID     |
| template_source | string   | NO    | source of flow，default value is business. business: from business, common: from common flow |
| id_in         |  string    | NO     | source id list of template, separated by `,` |
| name_keyword  |  string    | NO     | keyword of template name, ignore case |
| scope | string | NO | bk_biz_id scope. default value is 'cmdb_biz' and bk_sops will find a project which relate cmdb business id equal to bk_biz_id. otherwise, bk_sops will find a project which id equal to bk_biz_id when scope value is 'project'|

### Request Parameters Example

```
{
    "bk_app_code": "esb_test",
    "bk_app_secret": "xxx",
    "bk_token": "xxx",
    "bk_username": "xxx",
    "bk_biz_id": "2",
    "id_in": "1, 2, 3"
    "template_source": "business",
    "scope": "cmdb_biz",
    "name_keyword": "xxx"
}
```

### Return Result Example

```
{
    "result": true,
    "data": [
        {
            "category": "Other",
            "edit_time": "2018-04-23 17:30:48 +0800",
            "create_time": "2018-04-23 17:26:40 +0800",
            "name": "new111",
            "bk_biz_id": "2",
            "creator": "admin",
            "bk_biz_name": "blueking",
            "id": 32,
            "editor": "admin",
            "creator":"admin"
        },
        {
            "category": "Other",
            "edit_time": "2018-04-19 12:04:42 +0800",
            "create_time": "2018-04-19 12:04:42 +0800",
            "name": "new201804191218",
            "bk_biz_id": "2",
            "creator": "admin",
            "bk_biz_name": "blueking",
            "id": 31,
            "editor": null,
            "creator":"admin"
        },
        {
            "category": "Other",
            "edit_time": "2018-04-18 17:09:39 +0800",
            "create_time": "2018-04-16 21:43:15 +0800",
            "name": "new20180416213944",
            "bk_biz_id": "2",
            "creator": "admin",
            "bk_biz_name": "blueking",
            "id": 30,
            "editor": "admin",
            "creator":"admin"
        },
    ],
    "request_id": "xxx",
    "trace_id": "xxx"
}
```

### Return Result Description

| Field      | Type      | Description      |
|-----------|----------|-----------|
|  result   |    bool    |      true or false, indicate success or failure                      |
|  data     |    dict    |      data returned when result is true, details are described below  |
|  message  |    string  |      error message returned when result is false                     |
|  request_id     |    string  | esb request id         |
|  trace_id     |    string  | open telemetry trace_id       |

#### data

| Field      | Type      | Description      |
|-----------|----------|-----------|
|  bk_biz_id     |    string    |      the business ID      |
|  bk_biz_name   |    string    |      the business name    |
|  id            |    int       |      flow template ID             |
|  name          |    string    |      flow template name            |
|  category      |    string    |      flow template type, the value is described below    |
|  creator       |    string    |      person who created this flow template      |
|  create_time   |    string    |      datetime when this flow template created   |
|  editor        |    string or null | person who edited this flow template last |
|  edit_time     |    string    |      datetime when this flow template edited          |

#### data.category

| Value        | Description     |
|--------------|----------|
| OpsTools     | operation tools  |
| MonitorAlarm | monitor alarm  |
| ConfManage   | configuration management  |
| DevTools     | development tools  |
| EnterpriseIT | enterprise IT   |
| OfficeApp    | official APPs  |
| Other        | other     |
