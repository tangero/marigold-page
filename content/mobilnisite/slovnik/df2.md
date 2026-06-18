---
slug: "df2"
url: "/mobilnisite/slovnik/df2/"
type: "slovnik"
title: "DF2 – Delivery Function 2"
date: 2016-01-01
abbr: "DF2"
fullName: "Delivery Function 2"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/df2/"
summary: "DF2 je funkční entita v architektuře služby krátkých zpráv (SMS) dle 3GPP, konkrétně definovaná pro SMS v sítích GSM. Funguje jako zprostředkovatel, který přijímá a přeposílá SMS zprávy mezi centrem s"
---

DF2 je funkční entita v architektuře služby krátkých zpráv (SMS) dle 3GPP pro GSM, která funguje jako zprostředkovatel pro přeposílání zpráv mezi centrem služby krátkých zpráv (SM-SC) a ústřednou mobilního přepojování (MSC) za účelem zajištění spolehlivého doručení.

## Popis

Delivery Function 2 (DF2) je prvek jádra sítě specifikovaný v 3GPP TS 43.033 pro GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)). Funguje v rámci architektury služby krátkých zpráv ([SMS](/mobilnisite/slovnik/sms/)) jako klíčový přestupní bod. DF2 přijímá mobilním terminálem ukončené ([MT](/mobilnisite/slovnik/mt/)) SMS zprávy z centra služby krátkých zpráv (SM-SC) prostřednictvím bránové [MSC](/mobilnisite/slovnik/msc/) pro SMS ([SMS-GMSC](/mobilnisite/slovnik/sms-gmsc/)). Jejím hlavním úkolem je přeposlat tyto zprávy příslušné ústředně mobilního přepojování (MSC), která aktuálně obsluhuje cílovou mobilní stanici ([MS](/mobilnisite/slovnik/ms/)). To zahrnuje dotazování na domovský registrační uzel ([HLR](/mobilnisite/slovnik/hlr/)) za účelem získání směrovacích informací, konkrétně adresy MSC, aby byla zpráva doručena na správný obslužný síťový uzel.

Architektonicky je DF2 logická funkce, která může být umístěna společně s jinými síťovými prvky, jako je MSC nebo vyhrazená jednotka pro vzájemné propojení SMS. Rozhraní k SM-SC/SMS-GMSC využívá protokoly jako Mobile Application Part (MAP) pro signalizaci. Když je SMS předána do SM-SC, SMS-GMSC se dotazuje HLR na získání směrovacích informací. Pokud HLR indikuje, že účastník je dosažitelný, a poskytne adresu navštívené MSC (VMSC), SMS-GMSC přepošle zprávu DF2 asociované s touto oblastí MSC. DF2 poté doručí zprávu VMSC, která následně vyvolá mobilní stanici a doručí SMS přes rozhraní rádiového přístupu.

DF2 hraje klíčovou roli ve spolehlivosti a vzájemném propojení služby SMS. Zpracovává chybové scénáře, jako je dočasná nedostupnost účastníka, interakcí s HLR za účelem přijetí upozornění, když se účastník znovu stane dosažitelným (prostřednictvím funkce SMS Alert SC). Také spravuje převod a adaptaci protokolu, je-li to nutné, mezi MAP rozhraním od SM-SC a interní signalizací používanou v rámci MSC. Zatímco její funkce je v základním toku zpráv z velké části transparentní, její přítomnost je nezbytná pro oddělení bránové směrovací funkce (SMS-GMSC) od funkce finálního doručení, což umožňuje škálovatelné a řiditelné návrhy SMS sítí ve starších GSM systémech.

## K čemu slouží

DF2 byla vytvořena za účelem poskytnutí standardizovaného, spolehlivého mechanismu pro doručování zpráv služby krátkých zpráv (SMS) v rámci GSM sítí, jak je definováno ve specifikacích 3GPP Release 8 a starších. Před jejím formálním definováním ve specifikacích 3GPP byly mechanismy doručování SMS často proprietární nebo volně definované, což vedlo k potenciálním problémům s interoperabilitou mezi různými dodavateli síťového vybavení. Specifikace DF2 si kladla za cíl toto vyřešit jasným vymezením funkčních odpovědností mezi bránovým uzlem (SMS-GMSC), který směruje zprávy na základě dat z HLR, a doručovacím uzlem, který zajišťuje poslední úsek cesty k obslužné MSC.

K jejímu vzniku motivoval explozivní růst využívání SMS na konci 90. let a začátku 21. století, který vyžadoval robustnější a škálovatelnější architekturu jádra sítě. Definováním DF2 jako samostatné logické funkce umožnilo 3GPP síťovým operátorům nasazovat a škálovat prostředky pro doručování SMS nezávisle na bránových funkcích. Toto oddělení řešilo omezení starších implementací, kde bylo směrování a doručování SMS úzce provázáno, což mohlo vést k úzkým hrdlům a jediným bodům selhání. Standardizované rozhraní DF2 také usnadnilo hladší vzájemné propojení mezi SM-SC a MSC různých síťových operátorů, což bylo klíčové pro úspěch SMS zpráv mezi operátory.

## Klíčové vlastnosti

- Přeposílá mobilním terminálem ukončené SMS ze SMS-GMSC k obslužné MSC
- Komunikuje s HLR za účelem získání směrovacích informací pro doručení zprávy
- Zpracovává chybové stavy a scénáře nedostupnosti účastníka
- Podporuje funkci SMS Alert SC pro opakování doručení při dostupnosti účastníka
- Poskytuje standardizované rozhraní založené na MAP pro interoperabilitu
- Může být umístěna společně s MSC nebo implementována jako samostatný uzel

## Související pojmy

- [SMS-GMSC – Short Message Service Gateway MSC](/mobilnisite/slovnik/sms-gmsc/)

## Definující specifikace

- **TS 43.033** (Rel-13) — Lawful Interception Stage 2 for GSM/GPRS

---

📖 **Anglický originál a plná specifikace:** [DF2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/df2/)
