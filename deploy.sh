#!/bin/bash

# ===== CONFIGURATION =====
APP_NAME="blogging"
RESOURCE_GROUP="AppServicesGroup"
SUBSCRIPTION_ID="ef2a5cb2-a811-44b8-8426-7d437f63e90e"
ZIP_FILE="release.zip"
DEPLOY_DIR="."  # adjust if your code is in a subfolder

# ===== STEP 1: Login to Azure =====
echo "🔐 Logging into Azure..."
az account show &> /dev/null
if [ $? -ne 0 ]; then
    az login
fi

# ===== STEP 2: Set Subscription =====
echo "📌 Setting subscription to $SUBSCRIPTION_ID"
az account set --subscription "$SUBSCRIPTION_ID"

# ===== STEP 3: Create ZIP Package =====
echo "📦 Zipping files from $DEPLOY_DIR to $ZIP_FILE"
cd "$DEPLOY_DIR"
zip -r "../$ZIP_FILE" . -x "*.git*" -x "*__pycache__*" -x "*.venv*" > /dev/null
cd ..
echo "✅ Zip package created"

# ===== STEP 4: Deploy ZIP to App Service =====
echo "🚀 Deploying $ZIP_FILE to Azure Web App: $APP_NAME..."
az webapp deployment source config-zip \
  --resource-group "$RESOURCE_GROUP" \
  --name "$APP_NAME" \
  --src "$ZIP_FILE" \
  --subscription "$SUBSCRIPTION_ID"

if [ $? -ne 0 ]; then
    echo "❌ Deployment failed!"
    exit 1
fi

# ===== STEP 5: Show Deployment Log URL =====
echo "🔍 View deployment log:"
echo "   https://$APP_NAME.scm.azurewebsites.net/api/deployments/latest/log"

# ===== STEP 6 (Optional): Tail Logs =====
read -p "Do you want to tail the app logs now? (y/n): " tail_logs
if [[ "$tail_logs" == "y" ]]; then
    echo "📄 Tailing logs for app: $APP_NAME"
    az webapp log tail \
      --name "$APP_NAME" \
      --resource-group "$RESOURCE_GROUP"
fi