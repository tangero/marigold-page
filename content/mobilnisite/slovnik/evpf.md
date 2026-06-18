---
slug: "evpf"
url: "/mobilnisite/slovnik/evpf/"
type: "slovnik"
title: "EVPF – Enhanced Validity Period Format"
date: 2025-01-01
abbr: "EVPF"
fullName: "Enhanced Validity Period Format"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/evpf/"
summary: "Formát pro určení doby platnosti zpráv v SMS, který ve srovnání s původním formátem doby platnosti (VPF) nabízí jemnější granularitu a širší rozsah. Umožňuje přesnější řízení načasování doručení zpráv"
---

EVPF je rozšířený formát pro určení platnosti SMS zpráv, který ve srovnání s původním VPF poskytuje jemnější granularitu a širší rozsah.

## Popis

Enhanced Validity Period Format (EVPF) je standardizovaný mechanismus definovaný v 3GPP TS 27.005 pro určení doby platnosti zpráv služby krátkých zpráv ([SMS](/mobilnisite/slovnik/sms/)). Doba platnosti je klíčový parametr, který určuje, jak dlouho má centrum služby krátkých zpráv ([SMSC](/mobilnisite/slovnik/smsc/)) zkoušet doručit nedoručenou zprávu na mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) příjemce, než ji zahodí. EVPF ve srovnání se svým předchůdcem, formátem doby platnosti (VPF), poskytuje flexibilnější a rozšířené vyjádření časových intervalů.

Z architektonického hlediska EVPF funguje v rámci protokolového zásobníku SMS, konkrétně v protokolových datových jednotkách ([PDU](/mobilnisite/slovnik/pdu/)) SMS-SUBMIT a SMS-COMMAND. Když je odeslána SMS z mobilního zařízení, může zdrojová MS zahrnout parametr doby platnosti zakódovaný pomocí EVPF. Tento parametr následně interpretuje SMSC, který jej používá pro správu životního cyklu zprávy ve svých úložných a doručovacích frontách. Formát je navržen tak, aby byl zpětně kompatibilní a interoperabilní se systémy, které rozumějí pouze staršímu VPF.

Technicky EVPF kóduje dobu platnosti jako relativní časový odstup od okamžiku odeslání zprávy. Pro odlišení od staršího formátu používá specifický identifikátor informačního prvku v rámci SMS PDU. Kódování umožňuje mnohem širší škálu možných dob trvání, od velmi krátkých intervalů (např. minut) až po extrémně dlouhé (např. týdny nebo specifické absolutní časové značky v závislosti na variantě kódování). Toho je dosaženo efektivnějším využitím oktetů přidělených pro pole doby platnosti, často pomocí kombinace relativního a absolutního časového vyjádření podle definice ve specifikaci.

Jeho úlohou v síti je zlepšit řízení a efektivitu provozu SMS. Díky umožnění přesného nastavení platnosti mohou síťoví operátoři optimalizovat úložné zdroje SMSC, zabránit neomezeným pokusům o opětovné doručení nedoručitelných zpráv (např. na vypnuté zařízení) a poskytovat diferenciaci služeb. Například kritická výstraha může mít krátkou platnost, aby byla zajištěna včasná snaha o doručení, zatímco propagační zpráva může mít delší platnost. EVPF je základním prvkem pro pokročilé funkce SMS a spolehlivé služby zasílání zpráv v sítích 2G, 3G, 4G a 5G, protože SMS zůstává základní přenosovou službou.

## K čemu slouží

EVPF byl vytvořen, aby řešil omezení původního formátu doby platnosti (VPF) definovaného v raných specifikacích GSM. Původní VPF měl omezený rozsah a granularitu pro určení platnosti zprávy, často omezený maximálně na přibližně 63 hodin nebo několik dní s hrubými kroky (např. přírůstky po hodinách). To bylo nedostatečné pro mnoho komerčních a provozních případů použití, jako je plánování doručení zpráv na vzdálenou budoucnost nebo nastavení velmi přesné krátkodobé platnosti pro časově citlivé výstrahy.

Motivace vycházela z rostoucího a diverzifikovaného využití [SMS](/mobilnisite/slovnik/sms/) mimo jednoduchou komunikaci mezi osobami. Aplikace jako komunikace mezi stroji (M2M), servisní oznámení a přidané služby vyžadovaly sofistikovanější řízení životního cyklu zprávy. Operátoři potřebovali způsob, jak efektivněji řídit zahlcení úložišť [SMSC](/mobilnisite/slovnik/smsc/) přesným určením, jak dlouho má být nedoručená zpráva uchována. EVPF poskytl toto vylepšené řízení, což umožnilo nové modely služeb a zlepšilo využití síťových zdrojů.

Historicky byl EVPF představen v 3GPP Release 8 jako součást pokračujícího vývoje SMS, aby si tato služba udržela relevanci vedle paketově přepínaných služeb. Vyřešil problém definováním nového, výraznějšího formátu v rámci stávající struktury SMS [PDU](/mobilnisite/slovnik/pdu/) při zachování zpětné kompatibility. Sítě a zařízení podporující EVPF mohou využívat jeho rozšířené možnosti, zatímco ta, která jej nepodporují, mohou přejít k interpretaci výchozí nebo hrubší doby platnosti, čímž je zajištěna kontinuita služeb napříč různými generacemi síťové infrastruktury.

## Klíčové vlastnosti

- Rozšířený rozsah platnosti podporující doby trvání od minut až po několik týdnů
- Jemnější granularita v časové specifikaci ve srovnání se starším VPF
- Mechanismy zpětné kompatibility se sítěmi používajícími původní VPF
- Podpora relativního i absolutního časového vyjádření
- Efektivní kódování v rámci pole SMS TP-Validity-Period
- Umožňuje přesnou správu úložiště SMSC a doručovacích front

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [SMSC – Short Message Service Centre](/mobilnisite/slovnik/smsc/)
- [TPDU – Transport Protocol Data Unit](/mobilnisite/slovnik/tpdu/)

## Definující specifikace

- **TS 27.005** (Rel-19) — SMS Control Protocols for GSM/UMTS

---

📖 **Anglický originál a plná specifikace:** [EVPF na 3GPP Explorer](https://3gpp-explorer.com/glossary/evpf/)
