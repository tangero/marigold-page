---
slug: "adf"
url: "/mobilnisite/slovnik/adf/"
type: "slovnik"
title: "ADF – Accounting Data Forwarding"
date: 2025-01-01
abbr: "ADF"
fullName: "Accounting Data Forwarding"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/adf/"
summary: "ADF je síťová funkce 3GPP odpovědná za shromažďování, zpracování a přeposílání účetních a účtovacích dat ze síťových prvků do účtovacích systémů. Zajišťuje přesné vyúčtování spolehlivým zpracováním zá"
---

ADF je síťová funkce 3GPP, která shromažďuje, zpracovává a přeposílá účetní a účtovací data ze síťových prvků do účtovacích systémů, aby zajistila přesné vyúčtování.

## Popis

Funkce Accounting Data Forwarding (ADF) je standardizovaný síťový prvek v architektuře 3GPP, konkrétně definovaný jako součást rámce správy a účtování. Jejím hlavním úkolem je fungovat jako zprostředkovatel pro účetní a účtovací informace: shromažďuje nezpracovaná data z různých síťových funkcí ([NF](/mobilnisite/slovnik/nf/)) podílejících se na poskytování služeb – jako jsou [SMF](/mobilnisite/slovnik/smf/), [UPF](/mobilnisite/slovnik/upf/), [AMF](/mobilnisite/slovnik/amf/) a [PCF](/mobilnisite/slovnik/pcf/) v 5G – a přeposílá je ve zpracovaném formátu k Charging Function ([CHF](/mobilnisite/slovnik/chf/)) nebo systémům offline účtování. ADF zajišťuje integritu dat, aplikuje potřebné formátování nebo korelaci a zajišťuje spolehlivý přenos těchto klíčových účtovacích informací.

Z architektonického hlediska je ADF umístěn v rámci řídicí roviny a komunikuje se síťovými funkcemi prostřednictvím standardizovaných referenčních bodů. V systémech 5G komunikuje s architekturou založenou na službách (SBA) pomocí rozhraní založených na službách využívajících [HTTP](/mobilnisite/slovnik/http/)/2. Přijímá účtovací triggery a události ze síťových funkcí, které mohou zahrnovat začátek/konec relace, objem využití, časové trvání a specifické servisní události. ADF tyto události zpracovává, případně koreluje data z více zdrojů (např. koreluje události řídicí a uživatelské roviny pro stejnou relaci), aby vytvořil ucelené záznamy účtovacích dat ([CDR](/mobilnisite/slovnik/cdr/)) nebo záznamy událostí (EDR).

Vnitřní fungování ADF zahrnuje několik klíčových procesů: sběr událostí, validace dat, generování záznamů, ukládání do bufferu a přeposílání. Implementuje mechanismy pro detekci duplicit, správu sekvenčních čísel a zpracování chyb, aby zabránila ztrátě účtovacích dat. ADF může také aplikovat operátorské specifické politiky pro agregaci, filtrování nebo přeformátování dat před odesláním do účtovacího systému. Jeho návrh klade důraz na spolehlivost, protože ztracená účetní data přímo znamenají ztracené příjmy, a proto často zahrnuje trvalé úložiště a mechanismy opakování při neúspěšném přenosu.

V širší účtovací architektuře ADF spolupracuje s funkcí Charging Trigger Function (CTF), která je vestavěna do síťových funkcí pro detekci zpoplatnitelných událostí. ADF lze chápat jako centralizovanou nebo distribuovanou funkci, která agreguje výstupy CTF. Její role je klíčová pro scénáře offline (post-paid) i online (pre-paid/reálného času) účtování, ačkoliv se vzorce její interakce mohou lišit. Pro online účtování může ADF přeposílat průběžná účetní data do Online Charging System (OCS) pro reálnou kontrolu kreditu, zatímco pro offline účtování odesílá finalizované CDR k Charging Data Function (CDF).

## K čemu slouží

ADF byla zavedena, aby řešila rostoucí složitost a rozsah účtování v mobilních sítích, zejména při přechodu na paketově přepínané služby v 3G a později. Dřívější okruhově přepínané systémy měly relativně jednoduché účtovací modely založené na délce hovoru, ale nástup GPRS, IMS a různorodých datových služeb vyžadoval robustnější, spolehlivější a škálovatelnější metodu pro shromažďování a přeposílání širokého spektra účtovacích událostí z distribuovaných síťových prvků. ADF pro tento účel poskytuje standardizovanou, vyhrazenou funkci, která odděluje sběr účtovacích dat od hlavní servisní logiky v síťových funkcích.

Před svou formalizací bylo zpracování účtovacích dat často integrováno přímo do síťových prvků, což vedlo k nekonzistenci, proprietárním implementacím a problémům s korelací dat napříč různými síťovými doménami. To činilo fakturační systémy složitými a náchylnými k chybám. ADF standardizuje rozhraní a chování pro přeposílání účetních dat, čímž zajišťuje interoperabilitu mezi zařízeními od různých dodavatelů a zjednodušuje integraci s fakturačními systémy. Řeší problém spolehlivého doručování účtovacích informací v distribuované síti, kde jednotlivé síťové funkce nemají být zatěžovány složitostí komunikačních protokolů fakturačních systémů a odolností vůči chybám.

Dále ADF umožňuje pokročilé účtovací scénáře, jako je konvergované účtování (kombinace předplaceného a postpaid), sponzoring a účtování založené na QoS, tím, že poskytuje konzistentní bod pro shromažďování a korelaci mnohostranných účtovacích událostí. Její vznik byl motivován potřebou zajištění příjmů – tedy potřebou zajistit, aby byla každá zpoplatnitelná událost přesně zachycena a zafakturována – což je základním předpokladem obchodních modelů operátorů. Jak se sítě vyvíjely k 4G a 5G s podporou síťového řezání a architektur založených na službách, role ADF se přizpůsobila tak, aby zvládala účtování na síťový řez a komunikaci s cloud-nativními síťovými funkcemi založenými na mikroslužbách.

## Klíčové vlastnosti

- Shromažďuje účtovací události z více síťových funkcí prostřednictvím standardizovaných rozhraní
- Koreluje a formátuje nezpracovaná data událostí do záznamů účtovacích dat (CDR) nebo záznamů událostí (EDR)
- Zajišťuje spolehlivé, bezstratkové přeposílání účetních dat do účtovacích systémů
- Podporuje scénáře offline (post-paid) i online (reálného času) účtování
- Implementuje mechanismy bufferování, opakování a zpracování chyb pro zajištění doručení dat
- Může aplikovat operátorské specifické politiky pro agregaci, filtrování nebo přeformátování dat

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.334** (Rel-19) — ProSe Protocols and Procedures
- **TR 26.981** (Rel-19) — MBMS Provisioning & Content Ingestion Interface Study
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS

---

📖 **Anglický originál a plná specifikace:** [ADF na 3GPP Explorer](https://3gpp-explorer.com/glossary/adf/)
