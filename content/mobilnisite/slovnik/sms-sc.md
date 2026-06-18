---
slug: "sms-sc"
url: "/mobilnisite/slovnik/sms-sc/"
type: "slovnik"
title: "SMS-SC – Short Message Service - Service Centre"
date: 2025-01-01
abbr: "SMS-SC"
fullName: "Short Message Service - Service Centre"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sms-sc/"
summary: "SMS-SC je centrální síťový prvek zodpovědný za ukládání, přeposílání a směrování zpráv služby krátkých zpráv (SMS). Slouží jako rozbočovač pro veškerý provoz SMS a komunikuje s dalšími uzly jádra sítě"
---

SMS-SC je centrální síťový prvek zodpovědný za ukládání, přeposílání a směrování zpráv SMS, který funguje jako klíčový rozbočovač pro veškerý provoz SMS.

## Popis

SMS-SC (Short Message Service – Service Centre) je samostatná síťová entita v architektuře 3GPP, která slouží jako centrální přepojovací a řídicí bod pro zprávy [SMS](/mobilnisite/slovnik/sms/). Není to prvek orientovaný na účastníka, ale server jádra sítě, který komunikuje na jedné straně s [MSC](/mobilnisite/slovnik/msc/), [SGSN](/mobilnisite/slovnik/sgsn/), [MME](/mobilnisite/slovnik/mme/) a uzly IMS (přes [IP-SM-GW](/mobilnisite/slovnik/ip-sm-gw/)) a na straně druhé s [HLR](/mobilnisite/slovnik/hlr/)/[HSS](/mobilnisite/slovnik/hss/). Jeho primární funkcí je přijímat zprávy od odesílatele nebo externích aplikací, dočasně je ukládat, určovat trasu k příjemci a přeposílat je k doručení. Pokud je příjemce nedostupný, SMS-SC zprávu zařadí do fronty a na základě pravidel operátora zahájí opakované pokusy o doručení.

Z architektonického hlediska se SMS-SC připojuje k síti přes standardizovaná rozhraní, přičemž primárně používá protokol [MAP](/mobilnisite/slovnik/map/) pro komunikaci s prvky jádra sítě s přepojováním okruhů a paketů (MSC, SGSN, HLR) v sítích 2G/3G/4G a protokol Diameter nebo SIP pro komunikaci s 5G Core nebo IMS. Když SMS-SC přijme zprávu od mobilního účastníka (Mobile Originated), zpracuje ji, což může zahrnovat ověření platnosti účastníka, aplikaci servisní logiky (např. pro prémiové služby) a následně dotaz na HLR/HSS pro získání směrovacích informací (adresy MSC, SGSN nebo MME, které aktuálně obsluhují příjemce). Pro zprávy určené mobilnímu účastníkovi (Mobile Terminated) od externích aplikací (jako jsou novinové výstrahy) SMS-SC provádí stejný postup vyhledání trasy a doručení.

SMS-SC také zajišťuje nezbytné doplňkové funkce, jako je generování doručovacích hlášení, která se odesílají zpět odesílateli pro potvrzení úspěšného přijetí nebo oznámení selhání. Spravuje dobu platnosti zprávy, po jejímž uplynutí jsou nedoručené zprávy zahozeny. Dále je SMS-SC bránou pro přidané služby (VAS), které umožňují aplikace jako stahování vyzváněcích melodií, hlasování a mobilní bankovnictví tím, že poskytuje standardizované rozhraní (často protokol SMPP - Short Message Peer-to-Peer) pro externí aplikační servery. V sítích 5G komunikuje SMS-SC s funkcí SMSF (SMS Function), která adaptuje SMS pro přenos přes 5G Core, ale inteligence pro uložení a přeposlání a směrování zůstává z velké části v SMS-SC.

## K čemu slouží

SMS-SC byl vytvořen k řešení základního problému asynchronního zasílání zpráv s funkcí uložení a přeposlání v mobilních sítích. Bez centrálního servisního centra by doručení textové zprávy vyžadovalo, aby byli odesílatel a příjemce současně připojeni a dosažitelní v síti, což je nepraktické. SMS-SC odděluje vysílání od příjmu, ukládá zprávy, když je příjemce offline, a opakuje pokusy o doručení, čímž zajišťuje spolehlivost služby.

Historicky, jak SMS získávalo na popularitě v GSM, bylo potřeba centralizovaného řídicího bodu pro zvládnutí směrování mezi různými síťovými operátory (interworking), aplikaci fakturační logiky a efektivní správu přívalu zpráv. SMS-SC poskytl tuto centralizovanou inteligenci a komunikoval s HLR pro nalezení účastníků kdekoli na světě. Také umožnil komerční ekosystém přidaných služeb tím, že fungoval jako zabezpečená, kontrolovaná brána mezi mobilními operátory a poskytovateli obsahu třetích stran. Jeho vytvoření standardizovalo původně síťově specifickou implementaci, což umožnilo globální interoperabilitu a roaming služby SMS, což bylo klíčové pro celosvětový úspěch této služby.

## Klíčové vlastnosti

- Centrální funkce uložení a přeposlání pro zařazování zpráv do fronty a opakované pokusy o doručení
- Komunikuje s HLR/HSS pro získání směrovacích informací o účastníkovi
- Generuje a zpracovává hlášení o stavu doručení
- Brána pro externí aplikační servery přes protokoly jako SMPP
- Podporuje scénáře SMS od mobilního účastníka i SMS určené mobilnímu účastníkovi
- Spravuje dobu platnosti zpráv a zpracování chyb

## Související pojmy

- [SMS-PP – Short Message Service – Point to Point](/mobilnisite/slovnik/sms-pp/)
- [IP-SM-GW – IP Short Message Gateway](/mobilnisite/slovnik/ip-sm-gw/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [SMPP – Short Message Peer-to-Peer Protocol](/mobilnisite/slovnik/smpp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.142** (Rel-19) — Value-added Services for SMS Requirements
- **TR 22.942** (Rel-19) — SMS Value-Added Services Requirements
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- **TS 31.115** (Rel-19) — Secured Packet Structure for UICC Applications

---

📖 **Anglický originál a plná specifikace:** [SMS-SC na 3GPP Explorer](https://3gpp-explorer.com/glossary/sms-sc/)
