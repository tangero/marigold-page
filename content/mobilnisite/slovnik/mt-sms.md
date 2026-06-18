---
slug: "mt-sms"
url: "/mobilnisite/slovnik/mt-sms/"
type: "slovnik"
title: "MT-SMS – Mobile Terminated Short Message Service"
date: 2025-01-01
abbr: "MT-SMS"
fullName: "Mobile Terminated Short Message Service"
category: "Services"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/mt-sms/"
summary: "Směr služby krátkých zpráv (SMS) od sítě k zařízení, což je základní služba mobilních sítí pro doručování textových zpráv. Zahrnuje přijetí zprávy páteřní sítí od externí entity (např. jiného telefonu"
---

MT-SMS je směr služby krátkých zpráv (SMS) od sítě k zařízení, kdy páteřní síť přijme zprávu z externího zdroje a doručí ji cílovému mobilnímu zařízení.

## Popis

Mobile Terminated Short Message Service (MT-SMS) označuje příjem krátké zprávy mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) nebo uživatelským zařízením (UE). Je to jedna polovina obousměrné služby [SMS](/mobilnisite/slovnik/sms/), druhou je Mobile Originated SMS ([MO-SMS](/mobilnisite/slovnik/mo-sms/)). MT-SMS je služba typu store-and-forward (ulož a přepošli), kdy je zpráva, typicky textová, doručena od entity pro krátké zprávy ([SME](/mobilnisite/slovnik/sme/)) – jako je jiný mobilní uživatel, systém hlasové pošty nebo aplikační server – do mobilního zařízení příjemce prostřednictvím páteřní infrastruktury mobilní sítě.

Architektura pro MT-SMS zahrnuje několik síťových funkcí. V síti GSM/UMTS je centrální entitou centrum služby krátkých zpráv (SM-SC), které zprávy ukládá a přeposílá. Pro MT-SMS přijme SM-SC zprávu od odesílající SME a dotazuje se na domácím registru polohy ([HLR](/mobilnisite/slovnik/hlr/)) nebo domácím registru účastníků ([HSS](/mobilnisite/slovnik/hss/)), aby zjistil aktuálně obsluhující ústřednu mobilní komunikace ([MSC](/mobilnisite/slovnik/msc/)) nebo entitu pro správu mobility ([MME](/mobilnisite/slovnik/mme/)) cílového účastníka. SM-SC pak přepošle zprávu této obsluhující MSC (pro CS SMS přes GSM/UMTS) nebo MSC/IWF/MME (pro SMS přes IP v novějších generacích). Obsluhující MSC následně, je-li zařízení v klidovém stavu, vyvolá mobilní zařízení a doručí zprávu přes signalizační kanály (např. za použití protokolu Mobile Application Part (MAP) pro přenos a vrstev správy spojení a mobility pro doručení).

V sítích LTE a 5G, které jsou čistě paketové, se doručování SMS vyvinulo. Pro MT-SMS v LTE je zpráva doručována přes rozhraní SGs založené na IP mezi MME a MSC, což je součást mechanismu Circuit-Switched Fallback (CSFB) pro SMS, nebo přes IP-SM-GW (IP Short Message Gateway) za použití rozhraní SGd založeného na Diameter pro SMS přes IP (SMSIP). V 5G je MT-SMS nativně podporován jako služba založená na IP. Páteřní síť 5G (5GC) využívá funkci služby krátkých zpráv (SMSF) jako koncový bod pro SM-SC. SMSF komunikuje s AMF (Access and Mobility Management Function) za účelem doručení zprávy do UE přes signalizační spojení NAS (Non-Access Stratum), přičemž využívá služební rozhraní Nsmsf. Zpráva je transparentně přenášena přes referenční bod N1 mezi UE a AMF.

Technický postup pro MT-SMS zahrnuje několik vrstev. Na aplikační vrstvě je zpráva formátována podle parametrů TP (Transfer Protocol) definovaných v 3GPP TS 23.040. Síťové vrstvy zajišťují směrování, zabezpečení a spolehlivé doručení. Mezi klíčové protokoly patří MAP v legacy jádrech, Diameter pro SMSIP a HTTP/2 pro služební rozhraní v 5GC. Doručení je signalizační procedura, nevyžadující vyhrazený bearer uživatelské roviny, což umožňuje doručování SMS i když je zařízení v klidovém režimu nebo není zapojeno do hovorové či datové relace. Díky tomu jde o vysoce spolehlivou a všudypřítomnou službu. MT-SMS zůstává klíčovou službou pro komunikaci mezi lidmi, dvoufázové ověřování, služební oznámení a výstrahy typu machine-to-person, navzdory vzestupu OTT messagingových aplikací.

## K čemu slouží

MT-SMS byl vytvořen jako součást původní služby krátkých zpráv (SMS) v GSM s cílem umožnit spolehlivý, na síti založený systém textového zasílání zpráv. Jeho účelem bylo poskytnout jednoduchý komunikační kanál typu store-and-forward (ulož a přepošli), který byl nezávislý na hlasových hovorech a mohl dosáhnout účastníka i když byl jeho telefon vypnutý nebo dočasně mimo dosah sítě (zprávy byly uloženy a doručeny při dostupnosti). Řešil problém asynchronní, nenaléhavé textové komunikace v raných digitálních mobilních sítích.

Historická motivace pramení z vývoje standardu GSM na konci 80. a začátku 90. let 20. století. SMS byla zpočátku vedlejším doplňkem využívajícím volnou kapacitu signalizačních kanálů používaných pro建立ování hovorů a aktualizaci polohy. MT-SMS konkrétně umožnil síti iniciovat doručování informací účastníkovi, čímž umožnil služby jako oznámení o hlasové poště, zpravodajská upozornění a později interaktivní služby. Odstranil omezení pagingových systémů a numerických displejů tím, že poskytl obousměrnou možnost alfanumerického zasílání zpráv.

V průběhu následných releasů 3GPP se účel MT-SMS rozšířil a jeho implementace se vyvíjela, aby si udržela relevanci. S přechodem na čistě IP sítě v LTE a 5G, kde byly odstraněny tradiční okruhově spínané domény, vznikl zásadní problém: jak pokračovat v poskytování této všudypřítomné služby. To motivovalo vývoj SMS přes IP (SMSIP) a později nativní podporu SMS v 5GC prostřednictvím SMSF. MT-SMS dnes řeší problém univerzálního, interoperabilního a bezpečného doručování zpráv pro kritické služby (jako bankovní OTP, nouzová upozornění a oznámení operátora) napříč různými síťovými generacemi a architekturami, což zajišťuje zpětnou kompatibilitu a kontinuitu služeb při vývoji sítí.

## Klíčové vlastnosti

- Doručení typu store-and-forward (ulož a přepošli) zajišťuje přijetí zprávy i při dočasné nedostupnosti příjemce
- Využívá síťové signalizační kanály (nikoli bearery uživatelské roviny) pro efektivní a rozšířené doručování
- Podporováno napříč všemi generacemi mobilních sítí (GSM, UMTS, LTE, 5G) s vyvíjejícími se přenosovými mechanismy
- Umožňuje kritické služby jako dvoufázové ověřování, služební oznámení a nouzová upozornění
- Spoléhá se na prvky páteřní sítě jako SM-SC, HLR/HSS, MSC, MME, SMSF pro směrování a doručování
- Definováno komplexními specifikacemi 3GPP pokrývajícími servisní požadavky, protokoly a propojování

## Související pojmy

- [MO-SMS – Mobile Originated Short Message Service](/mobilnisite/slovnik/mo-sms/)
- [IP-SM-GW – IP Short Message Gateway](/mobilnisite/slovnik/ip-sm-gw/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 31.115** (Rel-19) — Secured Packet Structure for UICC Applications

---

📖 **Anglický originál a plná specifikace:** [MT-SMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mt-sms/)
