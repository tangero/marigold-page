---
slug: "ctf"
url: "/mobilnisite/slovnik/ctf/"
type: "slovnik"
title: "CTF – Charging Trigger Function"
date: 2026-01-01
abbr: "CTF"
fullName: "Charging Trigger Function"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ctf/"
summary: "Charging Trigger Function (CTF) je logická funkce v sítích 3GPP, která detekuje zpoplatnitelné události a generuje informace pro účtování a účetnictví. Je základní součástí Online Charging System (OCS"
---

CTF je logická funkce v sítích 3GPP, která detekuje zpoplatnitelné události a generuje informace pro účtování pro systémy Online a Offline Charging.

## Popis

Charging Trigger Function (CTF) je základní architektonický prvek definovaný v rámci účtovacího rámce 3GPP. Není to samostatný síťový uzel, ale logická funkce vestavěná do různých síťových entit poskytujících služby, jako je Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN), Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), Serving Gateway (S-GW), Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)), Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), Application Functions ([AF](/mobilnisite/slovnik/af/)) a uzly IP Multimedia Subsystem (IMS), například Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)). Primární role CTF spočívá v monitorování aktivity uživatele a sítě v reálném čase, identifikaci událostí podléhajících účtování na základě politik operátora a následném spuštění účtovacího procesu.

Provozně CTF funguje tak, že aplikuje účtovací pravidla a filtry na datové toky a signalizační zprávy, které zpracovává. Když dojde k předdefinované zpoplatnitelné události – například zahájení datové relace, zřízení IMS hovoru, doručení SMS nebo spotřebě určitého objemu dat – CTF zaznamená relevantní podrobnosti. Tyto podrobnosti zahrnují identifikátory účastníka (např. [IMSI](/mobilnisite/slovnik/imsi/), [MSISDN](/mobilnisite/slovnik/msisdn/)), identifikátory relace, časová razítka, identifikátory služeb, objemy dat, dobu trvání a informace o poloze. Pro offline účtování CTF shromažďuje tyto informace do Charging Data Records (CDR) nebo Charging Events a předává je funkci Charging Data Function (CDF) přes referenční bod Rf. Pro online účtování CTF interaguje přímo s funkcí Online Charging Function (OCF) přes referenční bod Ro, aby žádala o rezervace kvót a hlásila spotřebu kvót v reálném čase, což umožňuje okamžitou kontrolu kreditu.

Vnitřní logika CTF je řízena účtovacími politikami nastavenými operátorem, které definují, co představuje zpoplatnitelnou událost, příslušné tarify a požadovanou úroveň podrobností informací. Její implementace musí zajistit spolehlivost a integritu, protože generovaná data přímo ovlivňují fakturaci. Návrh CTF odděluje servisní logiku síťového uzlu od účtovací logiky, což umožňuje flexibilní a škálovatelné fakturační modely. Podporuje různé metody účtování, včetně účtování na základě události (např. za SMS), na základě relace (např. za hovor) a na základě objemu/doby trvání (např. za datový provoz).

V širší účtovací architektuře CTF funguje jako zdroj a iniciátor všech účtovacích informací. Její správná funkce je prvořadá pro celý fakturační řetězec. Rozhraní s jádrovými účtovacími systémy (OCS/OFCS) využívá standardizované protokoly založené na Diameter (rozhraní Ro a Rf), což zajišťuje interoperabilitu mezi zařízeními různých výrobců. Schopnost CTF generovat podrobné, korelované záznamy pro komplexní služby, jako jsou ty v IMS, je nezbytná pro moderní konvergentní fakturační systémy, které účtují za hlas, data, zprávy a obsah jednotným způsobem.

## K čemu slouží

CTF byla vytvořena, aby řešila základní obchodní potřebu přesných, spolehlivých a flexibilních účtovacích mechanismů v telekomunikačních sítích. Před standardizovanými účtovacími architekturami byly fakturační systémy často proprietární, těsně svázané s dodavateli ústředen a neschopné podporovat nové, paketové služby jako GPRS a později 3G/4G data. Tento nedostatek standardizace ztěžoval operátorům zavádět inovativní tarify, provádět kontrolu kreditu v reálném čase nebo implementovat složité účtovací scénáře vyžadované pro služby IP Multimedia Subsystem (IMS).

Zavedení CTF jako součásti účtovacího systému 3GPP ve verzi 5 a její zpřesnění v následujících verzích poskytlo jasný, standardizovaný model pro oddělení funkcí poskytování služeb od účtovacích funkcí. Toto oddělení umožnilo výrobcům síťového vybavení se soustředit na poskytování služeb a zároveň zajistit konzistentní, interoperabilní metodu pro generování fakturačních záznamů. CTF řeší problém detekce zpoplatnitelných událostí napříč heterogenní sítí skládající se z uzlů od více dodavatelů. Umožňuje operátorům implementovat různé obchodní modely, včetně předplacených (online charging) a postpaid (offline charging), z jediného spouštěcího bodu.

Navíc evoluce směrem k plně IP sítím a pokročilým komunikačním službám vyžadovala podrobnější a okamžitou schopnost účtování. CTF prostřednictvím svých definovaných interakcí s OCS umožnila okamžité kontroly kreditu a správu kvót, což je klíčové pro prevenci podvodů u předplacených služeb a pro nabízení funkcí kontroly utrácení zákazníkům. Její návrh podporuje účtování jakékoli služby detekovatelné sítí, což z ní dělá budoucí základní kámen pro zpoplatnění všeho od základní konektivity po 5G síťové řezy a aplikace edge computingu.

## Klíčové vlastnosti

- Detekuje a spouští účtování na základě zpoplatnitelných událostí v síťových uzlech
- Generuje standardizované Charging Data Records (CDR) pro offline fakturaci
- Interaguje v reálném čase s Online Charging System (OCF) pro kontrolu kreditu
- Podporuje více účtovacích modelů: na základě události, relace a objemu
- Je integrována jako logická funkce v různých síťových funkcích (PGW, SMF, CSCF atd.)
- Pro komunikaci s účtovacími systémy využívá protokoly Diameter (rozhraní Ro, Rf)

## Související pojmy

- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [OFCS – Offline Charging System](/mobilnisite/slovnik/ofcs/)
- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)

## Definující specifikace

- **TS 24.334** (Rel-19) — ProSe Protocols and Procedures
- **TR 28.816** (Rel-17) — Charging for 5G Cellular IoT
- **TS 28.849** (Rel-19) — CAPIF Phase2 Charging Study
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.253** (Rel-19) — Charging for Control Plane Data Transfer
- **TS 32.254** (Rel-19) — Charging for Northbound APIs
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 32.256** (Rel-19) — 5G Connection & Mobility Charging Spec
- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.271** (Rel-19) — 3GPP LCS Charging Management Spec
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.276** (Rel-19) — VCS Online Charging from Proxy Function
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [CTF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ctf/)
