---
category: kybernetická bezpečn
companies:
- Microsoft
- Google
date: '2025-10-27 23:54:00'
description: Kritická zranitelnost CVE-2025-59287 ve Windows Server Update Services
  je aktivně zneužívána útočníky proti desítkám organizací. Microsoft vydal nouzovou
  záplatu, ale neaktualizoval informace o probíhajících útocích.
importance: 4
layout: tech_news_article
original_title: Microsoft WSUS attacks hit 'multiple' orgs, Google warns - theregister.com
publishedAt: '2025-10-27T23:54:00+00:00'
slug: microsoft-wsus-attacks-hit-multiple-orgs-google-wa
source:
  emoji: 📰
  id: null
  name: Theregister.com
title: Microsoft WSUS pod aktivním útokem, varuje Google a další bezpečnostní týmy
url: https://www.theregister.com/2025/10/27/microsoft_wsus_attacks_multiple_orgs/
urlToImage: https://regmedia.co.uk/2024/04/19/shutterstock_bell.jpg
urlToImageBackup: https://regmedia.co.uk/2024/04/19/shutterstock_bell.jpg
---

## Souhrn

Kritická bezpečnostní chyba ve Windows Server Update Services (WSUS) s označením CVE-2025-59287 je aktivně zneužívána kybernetickými útočníky proti desítkám organizací. Google Threat Intelligence Group varuje před novou skupinou útočníků UNC6512, která využívá tuto zranitelnost ke vzdálenému spuštění kódu a exfiltraci dat. Microsoft sice vydal nouzovou záplatu, ale dosud neaktualizoval své bezpečnostní doporučení o probíhajících útocích.

## Klíčové body

- Zranitelnost CVE-2025-59287 umožňuje neautentizovaným útočníkům vzdálené spuštění libovolného kódu na zranitelných serverech
- Google potvrdil aktivní útoky nové skupiny UNC6512 proti "desítkám organizací"
- Postiženy jsou Windows Server verze 2012 až 2025 s aktivní rolí WSUS
- Americká agentura CISA přidala chybu do katalogu známých zneužívaných zranitelností
- Microsoft neaktualizoval své bezpečnostní doporučení a stále uvádí, že chyba nebyla veřejně zveřejněna ani zneužita

## Podrobnosti

Zranitelnost CVE-2025-59287 vzniká kvůli nebezpečné deserializaci nedůvěryhodných dat v systému Windows Server Update Services. WSUS je služba Microsoftu, která umožňuje správcům IT centralizovaně spravovat a distribuovat aktualizace Windows napříč podnikovou sítí. Útočníci mohou tuto chybu zneužít bez jakékoliv autentizace, což z ní činí obzvláště nebezpečnou hrozbu.

Google Threat Intelligence Group identifikoval novou skupinu útočníků označenou jako UNC6512, která aktivně zneužívá tuto zranitelnost. Po získání přístupu útočníci provádějí průzkum kompromitovaného systému a okolního prostředí pomocí série příkazů. Google také potvrdil, že došlo k exfiltraci dat z napadených systémů.

Microsoft vydal nouzovou záplatu krátce po objevení zranitelnosti a označil ji jako "pravděpodobně zneužitelnou". Společnost však odmítla odpovědět na dotazy ohledně hlášených útoků a neaktualizovala své bezpečnostní doporučení. Microsoft uvedl, že bezpečnostní bulletiny obvykle neaktualizuje po zveřejnění, pokud původní informace nebyly nepřesné.

Postiženy jsou pouze servery s aktivní rolí WSUS ve verzích Windows Server 2012 až 2025. Servery bez této role nejsou zranitelné. Bezpečnostní výzkumníci zaznamenali přibližně 100 000 pokusů o zneužití této chyby, což naznačuje rozsáhlou kampaň.

## Proč je to důležité

Tato situace představuje vážné bezpečnostní riziko pro podnikové prostředí využívající Windows Server. WSUS je kritická infrastrukturní služba používaná tisíci organizacemi po celém světě k správě aktualizací. Ironie spočívá v tom, že systém určený k zabezpečení serverů prostřednictvím aktualizací se sám stal vstupní branou pro útočníky.

Nesoulad mezi Microsoftovým veřejným stanoviskem a varováními předních bezpečnostních týmů včetně Google je znepokojující. Zatímco Microsoft stále uvádí, že chyba nebyla zneužita, nezávislé bezpečnostní týmy potvrzují aktivní útoky proti desítkám organizací. Tato komunikační mezera může vést k tomu, že správci IT podceňují naléhavost instalace záplaty.

Zařazení do katalogu Known Exploited Vulnerabilities agentury CISA znamená, že federální agentury USA mají povinnost záplatu nainstalovat v určeném časovém rámci. Soukromé organizace by měly následovat tento příklad a prioritizovat okamžitou instalaci bezpečnostní aktualizace na všech serverech s aktivní rolí WSUS.

---

[Číst původní článek](https://www.theregister.com/2025/10/27/microsoft_wsus_attacks_multiple_orgs/)

**Zdroj:** 📰 Theregister.com
