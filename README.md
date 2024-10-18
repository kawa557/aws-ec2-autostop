# AWS Lambda EC2 Shutdown

このプロジェクトは、AWSのLambda関数を使用して、タグ `[shutdown:true]` が付与されたEC2インスタンスを毎日日本時間の20時に停止するためのCloudFormationテンプレートとPythonコードです。

## 構成

- `template.yaml`
  - CloudFormationテンプレート。Lambda機能、IAMロール、CloudWatchイベントルールを定義し、スケジュールに基づいてLambdaを定期実行します。
- `stop_ec2.py`
  - タグ `[shutdown:true]` が付与されたEC2インスタンスの停止を行うLambda関数のPythonコード。

## 必須要件

- AWSアカウント
- AWS CLI
- Python
- boto3ライブラリ（AWS SDK for Python）

## デプロイ手順

1. テンプレートファイルをパッケージ化する
aws cloudformation package \
  --template-file template.yaml \
  --s3-bucket cf-templates-1jcq9sx4g1nyh-ap-northeast-1 \
  --output-template-file packaged-template.yaml
2. テンプレートを展開する
aws cloudformation deploy --stack-name Autostop-EC2-stack --template-file packaged-template.yaml --capabilities CAPABILITY_NAMED_IAM 