---
slug: "pie"
url: "/mobilnisite/slovnik/pie/"
type: "slovnik"
title: "PIE – Priority Information Element"
date: 2026-01-01
abbr: "PIE"
fullName: "Priority Information Element"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pie/"
summary: "Priority Information Element (PIE) je základní datové pole v signalizačních protokolech 3GPP používané k vyjádření relativní důležitosti nebo naléhavosti relace, přenosového kanálu (bearer) nebo zpráv"
---

PIE je datové pole v signalizaci 3GPP, které udává relativní důležitost relace nebo zprávy za účelem řízení alokace síťových prostředků a zajištění zvýhodněného zacházení pro kritické služby.

## Popis

Priority Information Element (PIE) není jediná, monolitická entita, ale konceptuální pole vložené do různých zpráv a datových struktur protokolů 3GPP. Jeho hodnota vyjadřuje úroveň priority, kterou síťové uzly používají pro rozhodování v reálném čase o zacházení s provozem. PIE se vyskytuje na více vrstvách a v různých doménách: na úrovni [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum) v signalizačních zprávách, jako je Service Request nebo [PDN](/mobilnisite/slovnik/pdn/) Connectivity Request; na úrovni [AS](/mobilnisite/slovnik/as/) (Access Stratum) pro řízení rádiových prostředků (Radio Resource Control, [RRC](/mobilnisite/slovnik/rrc/)); v parametrech QoS přenosového kanálu EPS/5GS (Allocation and Retention Priority, [ARP](/mobilnisite/slovnik/arp/)); a v signalizaci IMS (např. v hlavičkách [SIP](/mobilnisite/slovnik/sip/) pro tísňová volání nebo [MCPTT](/mobilnisite/slovnik/mcptt/)).

Když uživatelské zařízení (UE) iniciuje službu, například tísňové volání nebo vysokoprioritní službu pro kritickou činnost, zahrne specifickou hodnotu PIE do příslušné signalizační zprávy. Například v 5GS nastaví UE hodnotu „[5GSM](/mobilnisite/slovnik/5gsm/) priority“ v PDU SESSION ESTABLISHMENT REQUEST. Síťové uzly, včetně funkce pro správu přístupu a mobility (AMF), funkce pro správu relací (SMF) a gNodeB, tuto hodnotu PIE vyhodnotí. Na základě nastavených politik síť uplatní zvýhodněné zacházení. To může znamenat upřednostnění navázání RRC spojení pro toto UE před jinými UE, přijetí žádosti o zřízení relace i při přetížení sítě (vysoká úroveň priority ARP) a plánování rádiových prostředků pro jeho přenosové kanály s vyšší předností.

PIE funguje v součinnosti s dalšími mechanismy QoS. V jádru sítě je parametr ARP, který obsahuje úroveň priority, schopnost přerušení (pre-emption capability) a zranitelnost vůči přerušení (pre-emption vulnerability), klíčovou konkrétní podobou konceptu PIE pro přenosové kanály. Vysoká priorita ARP může vyvolat aplikaci specifických QoS politik funkcí pro pravidla politiky a účtování (PCRF/PCF). V přístupové síti RAN jsou identifikátor toku QoS (QFI) a identifikátor QoS pro 5G (5QI) mapovány na úrovně priority, které ovlivňují algoritmy plánování paketů v gNodeB. Výsledným celkovým efektem je, že datový tok označený vysokou prioritou PIE má ve srovnání s běžným best-effort provozem nižší latenci, vyšší spolehlivost a větší šanci na úspěšné zřízení relace i při přetížení sítě.

## K čemu slouží

PIE existuje, aby řešil základní problém nedostatku a souběhu (contention) prostředků ve sdílených mobilních sítích. Bez standardizovaného mechanismu pro rozlišení důležitosti provozu by se se všemi relacemi zacházelo stejně (best-effort), což by znemožnilo garantovat výkon pro služby, kde je časová citlivost a spolehlivost kritická. To je nepřijatelné pro veřejnou bezpečnost (tísňová volání, komunikace záchranných složek), pro síťovou řídicí signalizaci (která musí projít, aby byla udržena funkce sítě) a další prémiové služby definované operátorem.

Historicky měly rané celulární systémy omezenou podporu pro upřednostňování. Koncept se významně rozvinul se zavedením IMS a plně IP sítí ve 3GPP Rel-7 a později s LTE/EPC. Potřeba konzistentního, celoprovozního mechanismu označování priority se stala naléhavou se standardizací tísňových volání přes IMS, která vyžadují možnost přerušení a garantovaný přístup. PIE poskytuje tento společný „jazyk priority“, kterému rozumí uživatelské zařízení (UE), přístupová síť RAN, jádro sítě i servisní vrstva (IMS).

Navíc snaha o síťové řezy (network slicing) a podporu různých vertikálních odvětví (např. automobilový průmysl, průmyslový IoT) v 5G zvýšila potřebu sofistikovaného řízení priority. Různé řezy a služby mají zcela odlišné požadavky na latenci a spolehlivost. PIE, zejména jako součást 5QI a QoS profilu, umožňuje síti dynamicky aplikovat vhodnou strategii správy prostředků pro každou relaci nebo tok. Je klíčovým prvkem pro funkci „priority service“ definovanou v 3GPP, která zajišťuje, že autorizovaní uživatelé a služby mohou obdržet lepší výkon podle politiky operátora a regulačních požadavků.

## Klíčové vlastnosti

- Vložen do více vrstev protokolů (NAS, AS, IMS) pro celoprovozní signalizaci priority
- Řídí prioritu navazování RRC spojení a plánování rádiových prostředků
- Integrální součást parametru Allocation and Retention Priority (ARP) pro správu přenosových kanálů
- Používá se k odvození charakteristik QoS Class Identifier (QCI) / 5G QoS Identifier (5QI)
- Podporuje přerušení (vysokoprioritní relace mohou přerušit nízkoprioritní) a zranitelnost vůči přerušení
- Nezbytný pro zřizování tísňových relací IMS a služeb pro kritickou činnost (MCPTT, MCVideo)

## Související pojmy

- [ARP – Allocation and Retention Priority](/mobilnisite/slovnik/arp/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TR 22.950** (Rel-19) — Feasibility Study on Priority Service
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR

---

📖 **Anglický originál a plná specifikace:** [PIE na 3GPP Explorer](https://3gpp-explorer.com/glossary/pie/)
