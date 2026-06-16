# Firebase Integration Guide: Reusing Your "DLV Thong Lo 20" Project

Since you already have a Firebase project named **DLV Thong Lo 20**, we can reuse it to host your database! Follow these simple steps to activate **Cloud Firestore** and connect your live resident database to your portal.

---

## Step 1: Enable Cloud Firestore in your Console
To store the 79 unit records and user directory, we must enable the database inside your Firebase Project:

1. Open your browser and go to your **[Firebase Console](https://console.firebase.google.com/)**.
2. Click on your **DLV Thong Lo 20** project.
3. In the left-hand sidebar, click on **Build** -> **Firestore Database**.
4. Click the prominent **Create database** button.
5. **Security Rules Selection**:
   * For initial testing, select **Start in test mode** (this allows our python script and client dashboard to perform reads/writes without authentication hurdles).
   * Click **Next**, choose a database location (e.g., `asia-east2` for Thailand proximity, or standard `us-central`), and click **Enable**.

---

## Step 2: Download your Service Account Key (For python uploader)
To batch upload all 79 units and co-ownership names using our `firebase_uploader.py` script:

1. In the Firebase Console, click the **Gear Icon** (âï¸) next to *Project Overview* in the top left, and select **Project Settings**.
2. Go to the **Service Accounts** tab.
3. Select **Firebase Admin SDK** (it will default to Python).
4. Click the **Generate new private key** button at the bottom.
5. Save the downloaded `.json` file into your Google Drive folder:
   ð `G:\My Drive\ANTIGRAVITY PROJECTS\DLV 2.0`
6. Rename this file to exactly:
   ð **`serviceAccountKey.json`**
7. **Run the Uploader**:
   Open a terminal in your project directory and run:
   ```bash
   python firebase_uploader.py
   ```
   *The script will automatically detect the key, authenticate, and sync all your resident details building-wide in 2 seconds!*

---

## Step 3: Add your Web App Config (For index.html dashboard)
To let the portal load and display any of the 79 units dynamically:

1. Go back to your **Project Settings** -> **General** tab.
2. Scroll down to the **Your apps** section.
3. If no app exists, click **Add app** (select the **Web** icon `</>`), register it as "DLV 2.0 Portal", and click register.
4. You will see a `firebaseConfig` block. Copy those exact credentials:
   ```javascript
   const firebaseConfig = {
       apiKey: "YOUR_LIVE_API_KEY",
       authDomain: "dlv-thong-lo-20.firebaseapp.com",
       projectId: "dlv-thong-lo-20",
       storageBucket: "dlv-thong-lo-20.appspot.com",
       messagingSenderId: "...",
       appId: "..."
   };
   ```
5. Open [index.html](file:///g:/My%20Drive/ANTIGRAVITY%20PROJECTS/DLV%202.0/index.html) and search for the `firebaseConfig` object (around line 870). Paste your live credentials there!
6. **Save index.html**.

---

### That's It! ð
Once you perform these steps, your dashboard will load all data directly from your live Firestore database instead of the mock file. You can test any unit dynamically by visiting `http://localhost:8000/index.html`!
