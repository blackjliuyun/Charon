# Charon
https://github.com/Xyntax/POC-T

python3 Charon.py -eT -t 30 -f vuln.txt -s webshell_scan

python3 Charon.py -eT -t 30 -f vuln.txt -s-all struts2_all


SCRIPT_ALL_LIST = {
    'thinkphp5_all': ['thinkphp5_rce', 'thinkphp5_5010rce', 'thinkphp5_5023rce', 'thinkphp5_5152rce'],
    'struts2_all': ['struts2_003', 'struts2_005', 'struts2_008', 'struts2_009', 'struts2_013', 'struts2_015',
                    'struts2_016', 'struts2_019', 'struts2_032', 'struts2_033', 'struts2_037', 'struts2_045',
                    'struts2_046', 'struts2_048', 'struts2_048_1', 'struts2_052', 'struts2_053', 'struts2_dev'],
    'weblogic_all': ['weblogic_4852', 'weblogic_0638', 'weblogic_3510', 'weblogic_3248', 'weblogic_3506',
                     'weblogic_2628', 'weblogic_2893', 'weblogic_weak', 'weblogic_ssrf'],
    'joomla_all': ['jooml_videoflow_sqli', 'joomla_registrationpro_sqli', 'joomla_videogallerylite_sqli'],
    'jboss_all': ['jboss_adminconsole', 'jboss_EJBInvokerServlet', 'jboss_jbossmq_httpil', 'jboss_jmxconsole',
                  'jboss_JMXInvokerServlet', 'jboss_readonly', 'jboss_webconsole'],
}