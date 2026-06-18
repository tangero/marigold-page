---
slug: "vas-sms"
url: "/mobilnisite/slovnik/vas-sms/"
type: "slovnik"
title: "VAS-SMS – Value-added Services for SMS"
date: 2025-01-01
abbr: "VAS-SMS"
fullName: "Value-added Services for SMS"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vas-sms/"
summary: "Rámec 3GPP umožňující rozšířené služby krátkých textových zpráv (SMS) nad rámec základního zasílání zpráv mezi osobami. Standardizuje architekturu a rozhraní pro poskytovatele služeb třetích stran, kt"
---

VAS-SMS je standardizovaný rámec 3GPP, který definuje rozšířené služby SMS nad rámec základního zasílání zpráv. Umožňuje služby třetích stran, jako jsou upozornění a mobilní marketing, a vytváří tak pro operátory ekosystém generující příjmy.

## Popis

VAS-SMS je standardizovaný rámec v rámci 3GPP, který definuje architekturu a postupy pro poskytování služeb s přidanou hodnotou prostřednictvím služby krátkých textových zpráv ([SMS](/mobilnisite/slovnik/sms/)). Rozšiřuje základní infrastrukturu SMS, která je primárně navržena pro komunikaci mezi osobami (P2P), aby podporovala modely zasílání zpráv mezi aplikací a osobou ([A2P](/mobilnisite/slovnik/a2p/)) a mezi osobou a aplikací ([P2A](/mobilnisite/slovnik/p2a/)). Rámec specifikuje, jak se mohou externí poskytovatelé služeb s přidanou hodnotou ([VASP](/mobilnisite/slovnik/vasp/)) nebo vlastní servisní platformy operátora propojit s infrastrukturou SMS mobilní sítě, typicky prostřednictvím centra služby krátkých zpráv (SM-SC). Toto propojení se řídí standardizovanými rozhraními a protokoly, což zajišťuje interoperabilitu mezi různými síťovými operátory a poskytovateli služeb.

Architektura zahrnuje klíčové síťové prvky včetně SM-SC, které funguje jako úložný a přeposílací uzel pro SMS, a platformy VASP, která hostuje servisní logiku. Pro zprávy iniciované mobilním zařízením ([MO](/mobilnisite/slovnik/mo/)) určené pro službu s přidanou hodnotou směruje SM-SC zprávu na příslušného poskytovatele VASP na základě cílové adresy (např. zkráceného čísla). Pro zprávy doručované na mobilní zařízení ([MT](/mobilnisite/slovnik/mt/)) od poskytovatele VASP k účastníkovi předá VASP zprávu do SM-SC, které ji následně doručí prostřednictvím jádra sítě do mobilní stanice příjemce. Rámec také definuje servisní funkce, jako je prémiové zpoplatnění zpráv, kde jsou náklady na SMS vyšší než standardní sazba a výnosy jsou sdíleny mezi operátorem a poskytovatelem VASP.

Bezpečnost a účtování jsou kritické součásti. Rámec zahrnuje mechanismy pro souhlas účastníka, prevenci podvodů a přesné účtování. Podporuje různé modely účtování, včetně zpětného účtování, kdy náklady na zprávu nese poskytovatel služby nebo jsou přičteny k účtu účastníka. Úlohou VAS-SMS v síti je vytvořit bezpečný, účtovatelný a standardizovaný kanál pro inovativní služby, čímž transformuje SMS z jednoduchého komunikačního nástroje na platformu pro interaktivní služby, doručování informací a komerční transakce.

## K čemu slouží

VAS-SMS byl vytvořen, aby uvolnil komerční potenciál služby [SMS](/mobilnisite/slovnik/sms/) nad rámec jednoduchého zasílání textových zpráv. V počátcích mobilních sítí byla SMS základní, spolehlivá a téměř všudypřítomná služba. Operátoři a třetí strany rozpoznali příležitost využít této stávající infrastruktury k nabízení placených služeb, čímž by vytvořili nové zdroje příjmů. Účelem bylo standardizovat, jak lze tyto rozšířené služby integrovat do sítě bezpečným, interoperabilním a účtovatelným způsobem.

Před standardizací existovala proprietární řešení pro služby SMS s přidanou hodnotou, ale vedla k fragmentaci. Každý operátor mohl implementovat různá rozhraní a účtovací mechanismy, což ztěžovalo poskytovatelům služeb škálovat jejich nabídky napříč více sítěmi. Tento nedostatek interoperability brzdil inovace a růst trhu. Rámec 3GPP VAS-SMS to řešil definováním společných architektonických principů, referenčních bodů a postupů. Vyřešil problém, jak bezpečně připojit externí poskytovatele služeb k jádrové SMS síti, a zároveň zajistit spolehlivé doručování zpráv, přesné účtování a ochranu účastníka i síťového operátora před spamem a podvody.

## Klíčové vlastnosti

- Standardizovaná architektura pro SMS mezi aplikací a osobou (A2P) a mezi osobou a aplikací (P2A)
- Propojovací rozhraní mezi SM-SC a externími poskytovateli služeb s přidanou hodnotou (VASP)
- Podpora prémiově zpoplatněných zpráv s flexibilními modely sdílení výnosů
- Mechanismy pro souhlas účastníka a ochranu před nevyžádanou komunikací
- Integrace s účtovacími systémy jádra sítě pro přesné fakturace
- Spolehlivé doručování s funkcí ulož a přepošli prostřednictvím standardizovaného prvku SM-SC

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [VASP – Value Added Service Provider](/mobilnisite/slovnik/vasp/)

## Definující specifikace

- **TS 22.142** (Rel-19) — Value-added Services for SMS Requirements
- **TR 22.942** (Rel-19) — SMS Value-Added Services Requirements

---

📖 **Anglický originál a plná specifikace:** [VAS-SMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/vas-sms/)
