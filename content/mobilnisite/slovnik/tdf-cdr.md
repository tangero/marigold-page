---
slug: "tdf-cdr"
url: "/mobilnisite/slovnik/tdf-cdr/"
type: "slovnik"
title: "TDF-CDR – TDF generated Charging Data Record"
date: 2025-01-01
abbr: "TDF-CDR"
fullName: "TDF generated Charging Data Record"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tdf-cdr/"
summary: "Záznam účtovacích dat (Charging Data Record) generovaný funkcí TDF, obsahující podrobnosti o využití dat na aplikační úrovni. Používá se pro offline účtování a poskytuje přehled o tom, které aplikace"
---

TDF-CDR je záznam účtovacích dat (Charging Data Record) generovaný funkcí detekce provozu (Traffic Detection Function), který podrobně zaznamenává využití dat na aplikační úrovni pro offline účtování. Eviduje, které aplikace účastník použil a jakou spotřebu dat u nich měl.

## Popis

Záznam účtovacích dat generovaný funkcí [TDF](/mobilnisite/slovnik/tdf/) (TDF-CDR) je specifický typ [CDR](/mobilnisite/slovnik/cdr/) používaný v offline účtovacích systémech 3GPP. Vytváří jej funkce detekce provozu (Traffic Detection Function, TDF) nebo její spouštěcí funkce pro účtování (Charging Trigger Function, [CTF](/mobilnisite/slovnik/ctf/)) za účelem zaznamenání informací o využití souvisejících s detekcí a případnou kontrolou konkrétních aplikací. Na rozdíl od standardních CDR na úrovni přenosového kanálu (např. [S-CDR](/mobilnisite/slovnik/s-cdr/), [G-CDR](/mobilnisite/slovnik/g-cdr/)), které zaznamenávají objem a dobu trvání na [IP-CAN](/mobilnisite/slovnik/ip-can/) přenosový kanál, poskytuje TDF-CDR podrobné, na aplikaci zaměřené účtovací informace. Zaznamenává události, jako je zahájení a ukončení aplikačního toku, konkrétní detekovaná aplikace nebo služba (identifikovaná pomocí identifikátoru aplikace – Application Identifier) a objem dat přenesených pro danou aplikaci během detekčního období.

Generování TDF-CDR je spouštěno specifickými událostmi definovanými v pravidlech pro detekci a kontrolu aplikací (Application Detection and Control, [ADC](/mobilnisite/slovnik/adc/)), která poskytuje [PCRF](/mobilnisite/slovnik/pcrf/). Tato pravidla mohou TDF instruovat, aby vygenerovala CDR při zahájení nebo ukončení aplikační relace, nebo v pravidelných intervalech. Spouštěcí funkce pro účtování (CTF) v TDF shromažďuje relevantní účtovací informace, formátuje je podle specifikace 3GPP (TS 32.251) a přeposílá je funkci pro účtovací data (Charging Data Function, CDF) přes referenční bod Rf nebo Nchf (v 5G) pomocí protokolu Diameter. TDF-CDR obsahuje bohatou sadu polí včetně identity účastníka (např. IMSI, MSISDN), adresy TDF, času detekce, identifikátoru aplikace, nahlášených objemů dat (uplink a downlink) a případně použité QoS a účtovacích charakteristik.

V rámci širší účtovací architektury slouží TDF-CDR jako klíčový vstup pro fakturační a účetní systémy. Umožňují operátorům implementovat sofistikované účtovací modely založené na využití aplikací. Například operátor může nabízet „balíček pro sociální sítě“, kde data využitá službami Facebook a Twitter jsou zero-rated (neúčtují se), zatímco ostatní data se započítávají do měsíčního limitu. Fakturační systém koreluje TDF-CDR s dalšími CDR (jako jsou S-CDR) pomocí společného účtovacího ID (Charging ID), aby vytvořil úplný obraz o relaci účastníka. TDF-CDR je klíčovým prvkem pro diferenciaci služeb, který umožňuje operátorům překročit paušální účtování a vytvářet přidané, na aplikaci specifické tarify a poskytovat zákazníkům podrobné rozčlenění využití.

## K čemu slouží

TDF-CDR byl standardizován v 3GPP Release 12, aby vyřešil kritickou mezeru v účtovacích schopnostech: neschopnost účtovat na základě konkrétní používané aplikace nebo služby. Před jeho zavedením se účtovací systémy primárně spoléhaly na CDR na úrovni přenosového kanálu, které poskytovaly informace pouze o celkovém objemu dat na IP připojení (APN). To stačilo pro jednoduché objemové nebo časové účtování, ale bylo nedostatečné pro rostoucí trh nabídek služeb založených na aplikacích. Operátoři chtěli vytvářet inovativní datové tarify, jako jsou „pasy pro streamování videa“ nebo „balíčky hudebních služeb“, ale postrádali standardizovaný mechanismus pro měření a zaznamenávání spotřeby specifické pro aplikaci.

Vytvoření TDF-CDR tento problém vyřešilo tím, že poskytlo standardizovaný, interoperabilní formát pro hlášení využití na aplikační úrovni z TDF do offline účtovacího systému. Umožnilo nové obchodní modely a účtovací scénáře, které byly dříve nemožné nebo vyžadovaly proprietární, neintegrovaná řešení. Například umožňuje přesnou implementaci „sponzorovaných dat“, kde poskytovatel aplikace třetí strany platí za data využitá jeho službou, protože TDF-CDR jasně identifikuje aplikaci a její spotřebu dat.

Dále TDF-CDR podporuje regulatorní shodu a transparentnost. Poskytuje auditovatelný záznam o tom, které aplikace byly použity, což může být důležité pro fakturační spory nebo pro dodržování předpisů vyžadujících jasné sdělení o využití dat. Také umožňuje podrobné analýzy pro marketing a plánování sítě, protože operátoři mohou analyzovat trendy v oblíbenosti aplikací a vzorcích spotřeby. Standardizace TDF-CDR zajistila, že všichni dodavatelé sítí a poskytovatelé fakturačních systémů mohou vzájemně spolupracovat, což snižuje složitost pro operátory a podporuje konkurenční ekosystém pro řešení účtování s ohledem na aplikace.

## Klíčové vlastnosti

- Zaznamenává využití dat specifické pro aplikaci (objem dat v uplink/downlink)
- Obsahuje identifikátor aplikace (Application Identifier) pro detekovanou službu
- Obsahuje časová razítka pro zahájení/ukončení aplikační relace
- Koreluje s dalšími CDR relace pomocí účtovacího ID (Charging ID)
- Generován na základě spouštěčů definovaných v pravidlech ADC od PCRF
- Přenášen do CDF přes rozhraní Diameter Rf/Nchf pro offline účtování

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)

## Definující specifikace

- **TS 32.251** (Rel-19) — PS Domain Charging Management

---

📖 **Anglický originál a plná specifikace:** [TDF-CDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/tdf-cdr/)
