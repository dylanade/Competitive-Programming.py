class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = Counter()
        
        for cpdomain in cpdomains:
            count_visits, domain = cpdomain.split()
            subdomain_i = domain.find('.')
            subdomain_j = domain.rfind('.')
            
            count_visits = int(count_visits)
            domains[domain] += count_visits
            domains[domain[subdomain_i + 1:]] += count_visits
            
            if (subdomain_i != subdomain_j):
                domains[domain[subdomain_j + 1:]] += count_visits
                
        answer = []
        for domain, count in domains.items():
            answer.append(str(count) + ' ' + domain)
            
        return answer
                
        