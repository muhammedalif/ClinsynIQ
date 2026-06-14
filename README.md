# ClinsynIQ — Hospital Call Management System
**HealthionX Medical Solutions**

A Progressive Web App (PWA) for real-time ward call management. Ward staff submit call alerts; the Medical Officer on duty views and manages them in real time — across all devices.

---

## 🚀 Quick Setup

### Step 1 — Fork / Clone this repo
Push all files to a GitHub repo named `clinsyniq`.

### Step 2 — Firebase Setup (Required for multi-device sync)

1. Go to [console.firebase.google.com](https://console.firebase.google.com)
2. Click **Add project** → name it `clinsyniq` (or any name)
3. Disable Google Analytics (optional) → **Create project**
4. In the left panel → **Firestore Database** → **Create database**
   - Choose **Production mode** → select region (asia-south1 for India) → **Enable**
5. Go to **Project Settings** (⚙ gear icon) → **Your apps** → click **</>** (Web)
   - App nickname: `ClinsynIQ Web`
   - Click **Register app**
   - Copy the `firebaseConfig` object shown

6. Open `index.html` and replace the Firebase config block:
```javascript
const firebaseConfig = {
  apiKey           : "YOUR_API_KEY",          // ← paste here
  authDomain       : "YOUR_PROJECT.firebaseapp.com",
  projectId        : "YOUR_PROJECT_ID",
  storageBucket    : "YOUR_PROJECT.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",
  appId            : "YOUR_APP_ID"
};
```

### Step 3 — Firestore Security Rules
In Firebase Console → Firestore → **Rules** tab, paste:
```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /clinsyniq_calls/{doc} {
      allow read, write: if true;  // Open for hospital intranet use
    }
  }
}
```
> **Note:** For production, restrict by IP or add Firebase Auth.

### Step 4 — Customise the app
In `index.html`, edit the CONFIG block at the top of the `<script>`:
```javascript
const CONFIG = {
  hospitalName : "Kinder Hospital",   // ← your hospital name
  moPin        : "5678",              // ← change from default 1234
  wards: [
    // Edit this list to match your hospital's wards
    "General Ward", "ICU", "NICU", ...
  ]
};
```

### Step 5 — Enable GitHub Pages
- Go to repo **Settings** → **Pages**
- Source: `main` branch, root `/`
- Your app will be live at: `https://yourusername.github.io/clinsyniq/`

### Step 6 — Update manifest.json
Change the `start_url` and `scope` to match your GitHub Pages URL:
```json
"start_url": "/clinsyniq/",
"scope":     "/clinsyniq/"
```

---

## 📱 How to Use

### Ward Staff
1. Open the app on a ward tablet or phone
2. Tap **I'm Ward Staff**
3. Select ward, enter bed/patient, choose priority, describe the reason
4. Tap **Send Alert to MO** — done!

### MO on Duty
1. Open the app on your phone
2. Tap **I'm MO on Duty**
3. Enter the 4-digit PIN (default: `1234` — change in CONFIG)
4. View real-time colour-coded call log
5. Tap **On My Way** to acknowledge → **Attended** when done

---

## 🎨 Priority Colour Coding

| Priority | Colour | Use when |
|---|---|---|
| 🔴 Emergency | Red | Immediate life threat, cardiac arrest, acute deterioration |
| 🟡 Urgent    | Amber | Needs attention within 30 min, worsening parameters |
| 🟢 Non-urgent| Green | Review, prescription, routine query |

---

## ⚡ Features

- Real-time sync across all devices (Firebase Firestore)
- Sound + vibration alerts for new calls on MO dashboard
- Pulse animation for emergency calls
- Filter by status: All / Pending / Acknowledged / Attended
- Stats bar: live counts per priority
- Offline-capable (PWA with service worker)
- Install to home screen on iOS and Android
- Demo mode: works with local storage when Firebase not configured

---

## 🛠 Tech Stack

- Vanilla HTML/CSS/JS — zero dependencies, fast on any device
- Firebase Firestore — real-time NoSQL database (free Spark plan sufficient)
- Service Worker — offline support and PWA install
- Web Audio API — programmatic sound alerts (no audio files needed)
- Vibration API — haptic feedback for new alerts

---

## 📁 File Structure

```
clinsyniq/
├── index.html          ← Main app (all screens)
├── manifest.json       ← PWA manifest
├── sw.js               ← Service worker (offline support)
├── generate_icons.py   ← Run once to generate icons
└── icons/
    ├── icon-192.png    ← App icon (Android/PWA)
    └── icon-512.png    ← App icon (splash screen)
```

---

**HealthionX Medical Solutions** | Dr. Muhammed Alif | Consultant Anaesthesiologist & Intensivist
