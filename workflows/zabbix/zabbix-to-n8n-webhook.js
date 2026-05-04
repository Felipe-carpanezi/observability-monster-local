try {
    var params = JSON.parse(value),
        req = new HttpRequest(),
        response;

    req.addHeader('Content-Type: application/json');

    // URL do seu n8n que configuramos no Ingress
    var url = "http://n8n.127.0.0.1.sslip.io/webhook/zabbix-ai-trigger";

    var data = {
        event_id: params.eventid,
        event_name: params.eventname,
        hostname: params.hostname,
        severity: params.severity,
        error_msg: params.message
    };

    response = req.post(url, JSON.stringify(data));

    return response;
} catch (error) {
    Zabbix.log(3, 'n8n Webhook failed: ' + error);
    throw 'Webhook failed: ' + error;
}