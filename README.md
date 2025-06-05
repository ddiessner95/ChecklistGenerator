# ChecklistGenerator

A simple Blazor WebAssembly application to create and manage configurable checklists. All data is stored in the browser's local storage.

## Setup

You need the [.NET SDK](https://dotnet.microsoft.com/download) to run the app.

Restore dependencies and start the development server:

```bash
dotnet restore
dotnet run
```

The application will be available at `https://localhost:5001/` by default.

## Visual Studio

You can open the project in Visual Studio using the provided solution file:

1. Open **ChecklistGenerator.sln** in Visual Studio.
2. Press **F5** or choose **Debug > Start Debugging** to run the Blazor WebAssembly app.

## Features

- Create new checklists with any number of items
- View and update existing checklists
- Delete checklists

All data is persisted locally in your browser so no server setup is required.

