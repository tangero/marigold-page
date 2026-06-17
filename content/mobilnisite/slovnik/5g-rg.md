---
slug: "5g-rg"
url: "/mobilnisite/slovnik/5g-rg/"
type: "slovnik"
title: "5G-RG – 5G Residential Gateway"
date: 2026-01-01
abbr: "5G-RG"
fullName: "5G Residential Gateway"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/5g-rg/"
summary: "Zařízení typu CPE (customer premises equipment), které propojuje domácí nebo kancelářské sítě s 5G sítěmi a nahrazuje tradiční pevný širokopásmový přístup. Poskytuje místní síťovou konektivitu (Wi-Fi,"
---

5G-RG je zařízení na straně zákazníka, které propojuje domácí nebo kancelářské sítě s 5G sítí pro Fixed Wireless Access, poskytuje místní Wi-Fi a Ethernetovou konektivitu a jako backhaul využívá 5G.

## Popis

5G Residential Gateway (5G-RG) je standardizované zařízení na straně zákazníka definované 3GPP, které slouží jako koncový bod pro 5G konektivitu v domácím nebo kancelářském prostředí. Z architektonického hlediska funguje jako User Equipment (UE) s rozšířenými schopnostmi, připojuje se k 5G Core Network přes 5G Radio Access Network (gNB) a zároveň poskytuje služby místní sítě koncovým zařízením. 5G-RG obsahuje jak funkci 5G modemu pro bezdrátovou konektivitu, tak tradiční funkce routeru včetně Network Address Translation (NAT), firewallu, DHCP serveru a Wi-Fi přístupového bodu.

Z protokolového hlediska 5G-RG navazuje PDU Session s 5G Core Network, typicky pomocí IP PDU Session Type, a může podporovat více PDU Sessions pro různé služby nebo síťové řezy. Implementuje kompletní 5G UE protokolový stack včetně NAS signalizace pro správu mobility a správu relací, stejně jako nezbytné bezpečnostní procedury pro autentizaci a šifrování. Zařízení podporuje jak 3GPP, tak non-3GPP přístup, pokud je dostupný, ačkoli jeho primární funkcí je využití 5G NR jako backhaul připojení.

Klíčové komponenty v architektuře 5G-RG zahrnují 5G modemový modul s RF front-endem, směrovací engine se schopnostmi zpracování paketů, Wi-Fi subsystém (typicky podporující Wi-Fi 6 nebo novější) a rozhraní pro správu jak pro konfiguraci uživatelem, tak pro dálkovou správu od operátora. Zařízení podporuje TR-069 nebo ekvivalentní management protokoly pro dálkovou provizi, monitoring a aktualizace softwaru od poskytovatele služeb. Z pohledu sítě se 5G-RG jeví jako specializované UE se specifickými charakteristikami, které jej odlišují od mobilních telefonů, včetně odlišných požadavků na mobilitu, energetických profilů a očekávání služeb.

5G-RG hraje klíčovou roli při umožňování služeb Fixed Wireless Access (FWA) tím, že poskytuje most mezi 5G celulárními sítěmi a tradičními lokálními sítěmi. Podporuje mechanismy kvality služeb (QoS) pro zajištění odpovídajícího zacházení s různými typy provozu (hlas, video, data) přes bezdrátový spoj a implementuje schopnosti směrování provozu pro optimalizaci výkonu. Zařízení také podporuje povědomí o síťových řezech, což mu umožňuje navazovat připojení k různým síťovým řezům pro různé služby nebo smlouvy o úrovni služeb, ačkoli výběr řezu je typicky řízen síťovými politikami spíše než konfigurací uživatele.

## K čemu slouží

5G-RG byl vytvořen pro řešení rostoucí poptávky po flexibilním, vysokorychlostním širokopásmovém přístupu bez omezení spojených s nasazením fyzické infrastruktury. Tradiční pevný širokopásmový přístup vyžaduje rozsáhlou kabelovou instalaci (optika, měď), která je nákladná, časově náročná a geograficky omezená. 5G-RG umožňuje poskytovatelům služeb nabízet širokopásmové služby využívající stávající infrastrukturu 5G sítě, což dramaticky snižuje čas a náklady na nasazení, zejména v oblastech, kde položení kabelů je ekonomicky nebo fyzicky náročné.

Historicky byl domácí širokopásmový přístup poskytován prostřednictvím oddělených pevných a mobilních sítí s různými technologiemi, systémy správy a uživatelskými zkušenostmi. 5G-RG usnadňuje síťovou konvergenci tím, že umožňuje jedné 5G síti sloužit jak mobilním, tak pevným přístupovým potřebám, zjednodušuje síťové operace a umožňuje poskytovatelům služeb nabízet balíčkované služby. Tím řeší omezení předchozích přístupů, kdy pevné a mobilní sítě fungovaly odděleně s rozdílnými investičními cykly, provozními týmy a zákaznickými zkušenostmi.

Technologie také řeší potřebu zlepšeného pokrytí širokopásmovým přístupem v nedostatečně pokrytých oblastech, rychlé nasazení pro dočasné instalace a redundanci pro kritická připojení. Využitím vysoké přenosové kapacity, nízké latence a schopností síťových řezů 5G umožňuje 5G-RG poskytovatelům služeb nabízet diferencované širokopásmové služby se zaručenými výkonnostními charakteristikami. To představuje významný vývoj oproti dřívějším řešením Fixed Wireless Access založeným na 4G, poskytuje lepší výkon, efektivnější využití spektra a vylepšené možnosti správy díky těsnější integraci s architekturou 5G core sítě.

## Klíčové vlastnosti

- 5G NR konektivita s podporou jak sub-6 GHz, tak mmWave frekvenčních pásem
- Integrovaný Wi-Fi přístupový bod (typicky Wi-Fi 6/6E/7) pro distribuci místní sítě
- Více Ethernetových portů pro připojení kabelových zařízení
- Podpora síťových řezů a QoS diferenciace na PDU Session
- Možnosti vzdálené správy přes TR-069 nebo ekvivalentní protokoly
- Podpora duálního provozu IPv4 a IPv6

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.316** (Rel-19) — Wireline and Wireless Convergence Access Support
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.716** (Rel-16) — Wireline and Trusted Non-3GPP Access to 5G Core
- **TS 24.193** (Rel-19) — ATSSS Procedures Specification
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.413** (Rel-19) — NGAP for Non-3GPP Access
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.521** (Rel-19) — 5G Binding Support Management Service Stage 3
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3
- **TS 29.594** (Rel-19) — 5G Spending Limit Control Service Stage 3
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [5G-RG na 3GPP Explorer](https://3gpp-explorer.com/glossary/5g-rg/)
