---
slug: "sms-gmsc"
url: "/mobilnisite/slovnik/sms-gmsc/"
type: "slovnik"
title: "SMS-GMSC – Short Message Service Gateway MSC"
date: 2025-01-01
abbr: "SMS-GMSC"
fullName: "Short Message Service Gateway MSC"
category: "Core Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/sms-gmsc/"
summary: "SMS-GMSC je bránový MSC, který slouží jako vstupní bod pro mobilně-terminované krátké zprávy (MT-SM) z externího centra služby krátkých zpráv (SMSC) do jádra sítě GSM/UMTS. Dotazuje se HLR, aby získal"
---

SMS-GMSC je bránový MSC (Mobile Switching Centre), který slouží jako vstupní bod pro mobilně-terminované krátké zprávy (MT-SM) z externího SMSC. Pro jejich přeposlání dotazuje HLR (Home Location Register) o směrovací informace.

## Popis

SMS-GMSC (Short Message Service Gateway [MSC](/mobilnisite/slovnik/msc/)) je klíčová funkční entita v okruhově spínané ([CS](/mobilnisite/slovnik/cs/)) doméně jádra sítí 2G/3G, specificky definovaná pro doručování [SMS](/mobilnisite/slovnik/sms/). Jejím hlavním úkolem je sloužit jako brána pro mobilně-terminované krátké zprávy (MT-SM) vstupující do veřejné pozemní mobilní sítě ([PLMN](/mobilnisite/slovnik/plmn/)) z externího centra služby krátkých zpráv ([SMSC](/mobilnisite/slovnik/smsc/)). Když má SMSC zprávu určenou pro mobilního účastníka, odešle ji SMS-GMSC, typicky přes protokol [MAP](/mobilnisite/slovnik/map/) po [SS7](/mobilnisite/slovnik/ss7/) nebo IP spojích SIGTRAN. SMS-GMSC nemusí být fyzicky samostatný uzel; často jde o funkční roli implementovanou v rámci standardního ústředny MSC (Mobile Switching Centre).

Po přijetí MT-SM je prvním krokem SMS-GMSC dotaz na [HLR](/mobilnisite/slovnik/hlr/) (Home Location Register) za účelem získání směrovacích informací pro cílové telefonní číslo MSISDN. HLR odešle zprávu MAP_SEND_ROUTING_INFO_FOR_SM. HLR odpoví adresou aktuálně obsluhujícího MSC (MSC, kde je účastník momentálně registrován) a, je-li k dispozici, také číslem MSRN (Mobile Station Roaming Number). S těmito směrovacími informacemi pak SMS-GMSC přepošle krátkou zprávu na identifikované obsluhující MSC, které je zodpovědné za konečné doručení na mobilní zařízení přes rádiové rozhraní.

SMS-GMSC také řeší chybové stavy. Pokud HLR oznámí, že je účastník nedostupný nebo neznámý, SMS-GMSC informuje SMSC, které může zprávu uložit pro pozdější opakovaný pokus. Spravuje převod a adaptaci protokolů mezi rozhraním externího SMSC a interní signalizací MAP používanou v rámci PLMN. Ve vyspělých architekturách, jako je GSM/UMTS s IMS (IP Multimedia Subsystem), je role SMS-GMSC doplněna o IP-SM-GW pro SMS přes IP, ale pro tradiční doručování SMS v CS doméně zůstává klíčová. Její funkce zajišťuje, že SMSC, které může provozovat třetí strana, nepotřebuje přímou znalost dynamické polohy účastníka v síti, čímž zachovává abstrakci topologie sítě a soukromí účastníka.

## K čemu slouží

SMS-GMSC byl zaveden, aby oddělil externí centrum služby krátkých zpráv (SMSC) od vnitřní mobility a složitosti směrování v síti GSM/UMTS. Před jeho standardizací by SMSC potřebovalo přímou a aktuální znalost polohy každého účastníka pro doručení zpráv, což je kvůli mobilitě účastníků a změnám topologie sítě nepraktické. SMS-GMSC tento problém řeší tím, že slouží jako pevný, známý vstupní bod do sítě.

Jeho zavedení bylo motivováno potřebou škálovatelného, standardizovaného rozhraní pro propojení SMS. Umožňuje připojení více externích SMSC (stejného nebo různých operátorů) k PLMN přes jednu, dobře definovanou bránovou funkci. Tato architektura centralizuje kritický úkol dotazování HLR na směrovací informace a odlehčuje tím SMSC. Řeší omezení dřívějších proprietárních zprávových bran tím, že poskytuje standardizovaný 3GPP postup (signalizace MAP) pro získání směrovacích informací a přeposlání zprávy, což zajišťuje interoperabilitu mezi síťovými prvky různých výrobců a mezi sítěmi různých operátorů. SMS-GMSC je základním kamenem globálně interoperabilního ekosystému SMS.

## Klíčové vlastnosti

- Bránová funkce pro mobilně-terminované SMS z externích SMSC
- Dotazuje se HLR na směrovací informace účastníka pomocí protokolu MAP
- Přeposílá SMS na aktuálně obsluhující MSC na základě odpovědi z HLR
- Řeší chybové stavy a informuje SMSC o selhání doručení
- Poskytuje standardizovaný vstupní bod do PLMN, který abstrahuje vnitřní topologii sítě
- Často implementována jako funkční role v rámci fyzického uzlu MSC/VLR

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 29.338** (Rel-19) — Diameter protocols for SMS in MME/5GS
- **TS 32.622** (Rel-11) — Generic Network Resources IRP NRM
- **TS 32.632** (Rel-11) — Core Network Resources IRP: Network Resource Model
- **TS 32.732** (Rel-11) — IMS Network Resource Model IRP: Information Service

---

📖 **Anglický originál a plná specifikace:** [SMS-GMSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/sms-gmsc/)
