My name is Ehab Fakhralden Mohamed Hamid.

Registration number: 25/27950

App name: EFMHPortfolio

Verification code: MOB-A2-7950

Android package: rw.ac.ines.ug2527950.efmhportfolio

## Purpose

EFMHPortfolio is an offline Android portfolio for a recruiter. It introduces Ehab Fakhralden Mohamed Hamid, a Software Engineering student at INES-Ruhengeri, and shows programming work with Python, Java, C, and C++.

## Features

- Home screen with the required introduction, profile image, headline, biography, and verification code
- Skills list and an education timeline
- Four programming projects, each with a detail screen for the problem, contribution, and technology
- Profile editor with validation, field messages, and a blocked invalid save
- Camera or gallery selection, preview, replace, and remove for a profile image and a verification card
- Local save and reset with AsyncStorage, restored after the app restarts
- About screen with the app name, student name, registration number, verification code, version, and data-use statement
- Core screens work in Airplane Mode. The email link is marked Needs a connection

## Setup and run

```bash
npm install
npx expo start
```

Android development build:

```bash
npx expo run:android
```

Web preview:

```bash
npx expo start --web
```

## EAS build

The preview profile in `eas.json` produces an installable Android APK on an Expo account.

```bash
npx eas-cli login
npx eas-cli build -p android --profile preview
```

Install that APK on a phone and open it without Expo Go.

## Tested device

Physical-device results, including Airplane Mode, belong in `evidence/MOB_A2_27950_TEST_LOG.pdf` after the APK is installed. Fill in the phone model and Android version there before submission.

## Release record

- GitHub repository: https://github.com/Mogadi/MOB_A2_27950
- Release: https://github.com/Mogadi/MOB_A2_27950/releases/tag/v1.0.0
- APK: https://github.com/Mogadi/MOB_A2_27950/releases/download/v1.0.0/MOB_A2_27950.apk
- The release APK is a standalone arm64 build. It includes the JavaScript bundle and opens without Expo Go.
- Demonstration video: `MOB_A2_27950_DEMO.mp4` is recorded on a phone and attached to the same release. It is not stored in this repository.

## Known limitations

- Project descriptions are student programming work. Replace them in `src/data/portfolio.ts` if the final titles differ.
- The APK is attached to the GitHub release. This repository does not contain the APK binary.
- The demonstration video has to be recorded on a physical phone. It must be continuous, unedited, and no longer than two minutes.
- The email link needs a connection. The rest of the portfolio does not.

## Repository evidence

- `docs/MOB_A2_27950_UIUX.pdf`
- `evidence/MOB_A2_27950_TEST_LOG.pdf`
- `evidence/MOB_A2_27950_DECLARATION.pdf`
- `evidence/AI_USE.md`
