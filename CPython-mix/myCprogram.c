#include <stdio.h>

int main(int argc, char *argv[])
{
    if (argc < 4)
    {
        printf ("Please enter the server IP address"
                " and range of ports to be scanned\n");
        printf ("USAGE: %s IPv4 First_Port Last_Port\n", 
                argv[0]);
        exit(1);
    }
    char tIP[16] = {0};
    strcpy(tIP, argv[1]); // Copy the IPv4 address
    char First_Port[6] = {0};
    strcpy(First_Port, argv[2]); // Copy the start_port
    char Last_Port[6] = {0};
    strcpy(Last_Port, argv[3]); // Copy the end_port

    // Start port-scanner
    port_scanner(tIP, First_Port, Last_Port);
    return 0;
}