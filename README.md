# AWS Lambda EC2 Shutdown

このプロジェクトは、AWSのLambda関数を使用して、タグ `[shutdown:true]` が付与されたEC2インスタンスを毎日指定の時間に停止するためのCloudFormationテンプレートとPythonコードです。

## 構成

- `template.yaml`
  - CloudFormationテンプレート。Lambda機能、IAMロール、CloudWatchイベントルールを定義し、スケジュールに基づいてLambdaを定期実行します。
  - ParametersのScheduleExpressionで指定したcron式に従ってEC2を停止します。
    - cronで指定する時間はUTCです。
    - 例えばJST20時を指定する場合は"cron(0 11 * * ? *)" となります。
- `src/stop_ec2.py`
  - タグ `[shutdown:true]` が付与されたEC2インスタンスの停止を行うLambda関数のPythonコード。

## デプロイ手順

1. テンプレートファイルをパッケージ化する
aws cloudformation package \
  --template-file template.yaml \
  --s3-bucket cf-templates-1jcq9sx4g1nyh-ap-northeast-1 \
  --output-template-file packaged-template.yaml

2. テンプレートを展開する ※日本時間20時に停止する場合
aws cloudformation deploy \
  --stack-name Autostop-EC2-stack \
  --template-file packaged-template.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides ScheduleExpression="cron(0 11 * * ? *)"