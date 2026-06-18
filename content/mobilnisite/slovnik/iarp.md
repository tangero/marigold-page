---
slug: "iarp"
url: "/mobilnisite/slovnik/iarp/"
type: "slovnik"
title: "IARP – Inter-APN Routing Policy"
date: 2025-01-01
abbr: "IARP"
fullName: "Inter-APN Routing Policy"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/iarp/"
summary: "Soubor pravidel definovaných operátorem, která určují, jak je IP provoz z UE směrován mezi různými Access Point Names (APN). Umožňuje řízení a odklonění provozu na základě faktorů, jako je typ aplikac"
---

IARP je soubor pravidel definovaných operátorem, která určují, jak je IP provoz z UE směrován mezi různými Access Point Names (APN) za účelem řízení provozu na základě faktorů, jako je typ aplikace nebo cílová destinace.

## Popis

Inter-APN Routing Policy (IARP) je mechanismus správy sítě a řízení provozu definovaný ve standardech 3GPP, konkrétně v kontextu [ANDSF](/mobilnisite/slovnik/andsf/) (Access Network Discovery and Selection Function) a pozdějších vylepšení. Skládá se z politik nakonfigurovaných síťovým operátorem a poskytnutých uživatelskému zařízení (UE) za účelem inteligentního směrování toků IP provozu přes více současných připojení k paketové datové síti ([PDN](/mobilnisite/slovnik/pdn/)), z nichž každé je asociováno s jiným Access Point Name ([APN](/mobilnisite/slovnik/apn/)). APN definuje bránu ke konkrétní externí síti (např. internet, IMS síť nebo firemní intranet). Bez IARP typicky UE používá pro veškerý provoz výchozí APN nebo spoléhá na statickou konfiguraci, což je neefektivní pro moderní zařízení provozující více aplikací s různorodými požadavky.

Architektonicky jsou politiky IARP součástí širšího rámce ANDSF, který poskytuje UE informace o objevování sítí a politiky mobility mezi systémy ([ISMP](/mobilnisite/slovnik/ismp/)) nebo směrovací politiky ([ISRP](/mobilnisite/slovnik/isrp/)). IARP spadá do kategorie mezisystémových směrovacích politik při řešení směrování přes různá 3GPP a ne-3GPP přístupová rozhraní, ale konkrétně řídí směrování *mezi* APN přes stejný 3GPP přístup. Politiky jsou definovány ve formátu [XML](/mobilnisite/slovnik/xml/) (Managed Object) a jsou doručovány ze serveru ANDSF na UE přes referenční bod S14. Operační systém nebo software pro správu připojení v UE tyto politiky interpretuje a aplikuje je pro směrování odchozích IP paketů. Pravidla politiky mohou být založena na více kritériích, včetně cílové IP adresy nebo domény, aplikace (identifikované faktory jako ID aplikace v OS nebo případně číslo portu), požadované QoS nebo použité radiové přístupové technologie.

Fungování IARP zahrnuje, že UE vyhodnocuje svá aktivní PDN připojení a charakteristiky každého odchozího datového toku vůči poskytnutým pravidlům politiky. Například pravidlo může stanovit, že veškerý provoz určený pro doménu serveru korporátní [VPN](/mobilnisite/slovnik/vpn/) má být směrován přes APN 'corporate', zatímco obecný webový provoz používá APN 'internet'. Jiné pravidlo může nasměrovat vysokoprioritní provoz pro streamování videa na APN nakonfigurované pro QoS se zaručenou přenosovou rychlostí. UE tato rozhodnutí o směrování provádí na IP vrstvě, efektivně vážouce konkrétní sockety nebo toky na konkrétní síťová rozhraní (každé odpovídající PDN připojení). To umožňuje současné použití více APN, což vede k segregaci provozu, optimalizovanému účtování (např. oddělení zpoplatněného a nezpoplatněného provozu) a zlepšenému výkonu díky sladění potřeb aplikací s možnostmi síťového řezu nebo APN.

## K čemu slouží

IARP byl vytvořen, aby řešil omezení připojení s jedním [APN](/mobilnisite/slovnik/apn/) v éře stále sofistikovanějších mobilních zařízení a různorodých služeb. Rané systémy mobilních dat typicky přiřazovaly UE jedno výchozí APN pro veškerý internetový provoz. Tento monolitický přístup se stal neefektivním, když operátoři zaváděli specializovaná APN pro služby jako IMS (pro VoLTE), operátorské aplikace pro zasílání zpráv nebo partnerství s poskytovateli obsahu. Bez dynamického směrovacího mechanismu museli uživatelé ručně přepínat APN nebo zařízení mohla používat pouze jednu službu najednou, což vedlo ke špatnému uživatelskému zážitku a neschopnosti využít síťové optimalizace.

Primární problém, který IARP řeší, je inteligentní řízení provozu a optimalizace síťových prostředků. Umožňuje operátorům implementovat služebně-aware směrování, které směruje provoz k nejvhodnější síťové bráně na základě typu služby. To přináší několik výhod: odklonění určitého provozu (např. streamování videa) na APN optimalizované pro content delivery network za účelem snížení zatížení jádra sítě, zajištění, že provoz kritický pro podnikání používá zabezpečené APN se zaručenou QoS, a oddělení účtování směrováním 'sponzorovaného' obsahu přes APN s nulovým ratingem. Poskytuje standardizovanou, politikami řízenou alternativu ke komplexním a škálovatelným řešením, jako je deep packet inspection (DPI) v síti, nebo závislosti na zařízení-specifických proprietárních API pro správu připojení.

Zavedený v 3GPP Release 12, vývoj IARP byl motivován potřebou detailnější správy provozu jako součásti širších vylepšení ANDSF pro plynulé odkládání na Wi-Fi a koordinaci více přístupů. Představoval posun směrem k inteligenci v uživatelské rovině na zařízení, řízené síťovými politikami, což je v souladu s trendem software-defined networking (SDN) a virtualizace síťových funkcí (NFV). Tím, že IARP umožňuje UE činit rozhodnutí o směrování, snižuje signalizační zátěž v jádru sítě ve srovnání se síťově řízeným směrováním a umožňuje rychlejší a více aplikacím odpovídající správu provozu, čímž připravuje cestu pro pozdější koncepty, jako je multi-access edge computing (MEC) a síťové řezy v 5G, kde je směrování provozu zásadní.

## Klíčové vlastnosti

- Operátorem definované politiky založené na XML, poskytované UE přes ANDSF
- Směruje toky IP provozu mezi více současnými PDN připojeními (APN)
- Pravidla politik založená na kritériích, jako je cílová IP/doména, ID aplikace nebo požadavky na QoS
- Umožňuje služebně-aware řízení provozu pro optimalizaci a odkládání
- Podporuje segregaci provozu pro zabezpečení, účtování a výkonovou izolaci
- Vynucování na straně UE snižuje režii signalizace v jádru sítě

## Související pojmy

- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)
- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [ISRP – Inter-System Routing Policies](/mobilnisite/slovnik/isrp/)

## Definující specifikace

- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification

---

📖 **Anglický originál a plná specifikace:** [IARP na 3GPP Explorer](https://3gpp-explorer.com/glossary/iarp/)
