---
slug: "apn-ni"
url: "/mobilnisite/slovnik/apn-ni/"
type: "slovnik"
title: "APN-NI – Access Point Name Network Identifier"
date: 2025-01-01
abbr: "APN-NI"
fullName: "Access Point Name Network Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/apn-ni/"
summary: "APN-NI je část názvu přístupového bodu (Access Point Name, APN) označovaná jako síťový identifikátor. Toto klíčové označení se používá v sítích 3GPP k určení brány paketové datové sítě (PDN gateway) a"
---

APN-NI je část názvu přístupového bodu (Access Point Name) označovaná jako síťový identifikátor, která určuje bránu paketové datové sítě a externí síť, ke které se uživatelské zařízení připojuje pro směrování datového provozu.

## Popis

Síťový identifikátor názvu přístupového bodu (Access Point Name Network Identifier, APN-NI) je základní součást struktury [APN](/mobilnisite/slovnik/apn/) definované ve specifikacích 3GPP. APN je plně kvalifikovaný doménový název ([FQDN](/mobilnisite/slovnik/fqdn/)), který síť používá k výběru brány paketové datové sítě ([PGW](/mobilnisite/slovnik/pgw/)) pro kontext paketového datového protokolu ([PDP](/mobilnisite/slovnik/pdp/)) nebo připojení [PDN](/mobilnisite/slovnik/pdn/) uživatelského zařízení (UE). Samotný APN se skládá ze dvou částí: síťového identifikátoru APN (APN-NI) a operátorského identifikátoru APN ([APN-OI](/mobilnisite/slovnik/apn-oi/)). APN-NI je povinná část, která identifikuje externí paketovou datovou síť (PDN), se kterou si UE přeje komunikovat, například 'internet', 'ims' nebo firemní doménu jako 'company.mnc012.mcc345.gprs'. Volitelný APN-OI definuje doménu síťového operátora (např. .mnc<[MNC](/mobilnisite/slovnik/mnc/)>.mcc<[MCC](/mobilnisite/slovnik/mcc/)>.gprs) a je často připojována sítí.

Z architektonického hlediska se APN-NI používá během procedur navazování relace, především při aktivaci kontextu paketového datového protokolu (PDP) v GPRS/UMTS nebo při žádosti o připojení PDN v LTE/5G. Když UE zahájí datovou relaci, zahrne do signalizačních zpráv odeslaných do sítě požadovaný APN, který obsahuje APN-NI. Tuto žádost přijme podpůrný uzel GPRS (SGSN) v 2G/3G nebo entita pro správu mobility (MME)/funkce pro správu přístupu a mobility (AMF) v 4G/5G. Síťový uzel pak použije APN-NI spolu s informacemi z profilu účastníka z domácího registračního serveru (HSS) nebo jednotné správy dat (UDM) k určení vhodné brány PGW nebo funkce uživatelské roviny (UPF), která zajišťuje připojení k požadované externí síti.

Proces určení zahrnuje dotaz do doménového systému jmen (DNS). Síť sestaví plný APN FQDN potenciálním spojením APN-NI poskytnutého UE s operátorským APN-OI. Tento FQDN je následně dotazován v DNS, aby se získala IP adresa (adresy) vhodné brány PGW. Výběr je založen na faktorech, jako jsou schopnosti PGW, vytížení a topologická blízkost. APN-NI je tedy klíčem, který umožňuje mapování na konkrétní bránu a externí datovou síť. Umožňuje segmentaci sítě, což operátorům dovoluje nabízet odlišné služby (např. přístup k internetu, IMS pro VoLTE, podnikové VPN) přes stejnou fyzickou infrastrukturu pomocí různých APN-NI.

V architektuře jádra sítě je APN-NI úzce integrováno s řízením politik. Funkce pravidel pro účtování a zásady (PCRF) nebo funkce řízení politik (PCF) mohou být informovány o používaném APN. To umožňuje aplikaci specifických profilů kvality služeb (QoS), pravidel účtování a zásad řízení přístupu šitých na míru danému konkrétnímu APN-NI. Například provoz na APN-NI 'ims' může mít vyšší prioritu a jiné účtování než provoz na obecném APN-NI 'internet'. APN-NI tedy nepůsobí pouze jako směrovací štítek, ale také jako ukotvovací bod pro zásady v rámci systému 3GPP.

## K čemu slouží

APN-NI bylo vytvořeno, aby vyřešilo základní problém identifikace a připojení k různorodým externím paketovým datovým sítím z jádra sítě mobilního operátora. V raných sítích 2G GPRS, když operátoři začali nabízet datové služby přesahující jednoduchý přístup k internetu, byl potřebný mechanismus pro nasměrování uživatelského provozu na správnou cílovou síť, jako je brána WAP (Wireless Application Protocol), podniková intranetová síť nebo později subsystém IP multimédií (IMS). Bez standardizovaného identifikátoru, jako je APN-NI, by sítě postrádaly schopnost podporovat více souběžných datových služeb pro jednoho účastníka nebo nabízet specializované síťové řezy pro různé aplikace.

Historicky, před formalizací struktury APN, bylo datové připojení často monolitické nebo vyžadovalo proprietární konfigurace. Zavedení APN s APN-NI jako jeho klíčovým identifikátorem poskytlo standardizovanou, flexibilní a škálovatelnou metodu pro diferenciaci služeb. Odstranilo omezení spočívající v jediné univerzální datové cestě tím, že umožnilo síti vybírat různé brány (GGSN/PGW) na základě požadované služby. To bylo klíčové pro komercializaci mobilních dat, protože umožnilo vytváření služebně specifických APN s přizpůsobenými charakteristikami šířky pásma, zabezpečení a účtování.

Účel APN-NI sahá až k umožnění činnosti virtuálních mobilních operátorů (MVNO) a usnadnění roamingu. MVNO může použít vlastní APN-NI k směrování provozu přes vlastní síťovou infrastrukturu, i když využívá radiový přístup hostitelského operátora. Pro roamující účastníky navštívená síť použije APN-NI, často ve spojení s APN-OI domácího operátora, k navázání spojení zpět k bráně PGW domácí sítě (provoz směrovaný domů) nebo k místní bráně PGW (místní průnik), jak je definováno konfigurací APN. APN-NI je tedy základním kamenem pro inovace služeb, multi-tenancy a globální interoperabilitu v mobilních paketových sítích.

## Klíčové vlastnosti

- Identifikuje externí paketovou datovou síť (PDN) pro připojení uživatelského zařízení (UE)
- Povinná součást plně kvalifikovaného doménového jména (FQDN) názvu přístupového bodu (APN)
- Používají ji síťové uzly (SGSN/MME/AMF) k výběru vhodné brány PGW/UPF prostřednictvím DNS překladu
- Umožňuje diferenciaci služeb a segmentaci sítě (např. internet, IMS, podnikové VPN)
- Slouží jako klíč pro aplikaci služebně specifických zásad QoS a účtování prostřednictvím PCRF/PCF
- Podporuje roamingové scénáře tím, že usnadňuje směrování provozu domů nebo místní průnik

## Související pojmy

- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [PDN – Packet Data Network](/mobilnisite/slovnik/pdn/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)
- [DNS – Directory Name Service](/mobilnisite/slovnik/dns/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [APN-NI na 3GPP Explorer](https://3gpp-explorer.com/glossary/apn-ni/)
