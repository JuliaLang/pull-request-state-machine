# Deploying

## Developing

### Requirements

1. NPM
2. Python 3.8

### Instructions

##### Step 1:
Install dependencies:
```bash
npm install -g serverless
npm install
```

##### Step 2:
Set the secret environment variables:
```bash
export AWS_ACCESS_KEY_ID=my_id
export AWS_SECRET_ACCESS_KEY=my_key
export GITHUB_TOKEN=my_token
```

##### Step 3:
Deploy:
```bash
serverless deploy
```

##### Step 4:
Shutdown:
```bash
serverless remove
```
