import ssl
import OpenSSL
import datetime
from optparse import OptionParser
import sys
import socket


def get_cert_from_endpoint(server, port):
    result = None
    try:
        context = ssl.create_default_context()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sslSocket = context.wrap_socket(s, server_hostname = server)
        sslSocket.connect((server, port))
        after=sslSocket.getpeercert()['notAfter']
        sslSocket.close()
        ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
        return (datetime.datetime.strptime(after, ssl_date_fmt))
    except:
        result= None
    if not result:
        try:
            cert = ssl.get_server_certificate((server, port))
            result = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
            after = ''.join(filter(str.isdigit, str(result.get_notAfter())))
            return (datetime.datetime.strptime(after, "%Y%m%d%H%M%S"))
        except:
            return None


def get_cert_from_file(file_name):
    with open(file_name) as f:
        f = open(file_name)
        cert = f.read()
    result = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    after = ''.join(filter(str.isdigit, str(result.get_notAfter())))
    # return datetime.datetime(after)
    return (datetime.datetime.strptime(after, "%Y%m%d%H%M%S"))



def get_domain_days(domain,port):
    today=datetime.datetime.today()
    ssl_expired_date = get_cert_from_endpoint(domain,port)
    # print(ssl_expired_date)
    if not ssl_expired_date:
        return 10000
    else:
        print(ssl_expired_date)
        return (ssl_expired_date-today).days


if __name__ == '__main__':
    domains = []
    parser = OptionParser()
    parser.set_usage('\n    获取域名证书过期时间\n'
                     '    域名：python get_ssl_date.py -d <domain name>  \n'
                     '    证书文件: python get_ssl_date.py -f <ssl file> \n')
    parser.add_option('-d', '--domain', dest='domainName', help='输入域名')
    parser.add_option('-f', '--file', dest='fileName', help='输入文件名')
    options, arg = parser.parse_args()

    if (not options.domainName and not options.fileName):
        parser.print_help()
        exit()

    if (options.domainName and options.fileName):
        print('只允许同时检查域名或者证书其中一个\n')
        parser.print_help()
        exit()

    if options.domainName:
        domains.append(options.domainName)
        domains = domains + arg
        for item in domains:
            print(get_cert_from_endpoint(item))

    if options.fileName:
        domains.append(options.fileName)
        domains = domains + arg
        for item in domains:
            print(get_cert_from_file(item))