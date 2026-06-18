---
slug: "ip-sm-gw"
url: "/mobilnisite/slovnik/ip-sm-gw/"
type: "slovnik"
title: "IP-SM-GW – IP Short Message Gateway"
date: 2025-01-01
abbr: "IP-SM-GW"
fullName: "IP Short Message Gateway"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ip-sm-gw/"
summary: "Síťová funkce umožňující interoperabilitu mezi zastaralou službou krátkých textových zpráv (SMS) v přepojování okruhů a zasíláním zpráv po IP, primárně pro doručování zařízením připojeným přes IP sítě"
---

IP-SM-GW je síťová funkce, která zprostředkovává interoperabilitu mezi zastaralými SMS v přepojování okruhů a zasíláním zpráv po IP, přičemž funguje jako překladač protokolů a umožňuje doručování SMS přes IP sítě jako je IMS.

## Popis

IP Short Message Gateway (IP-SM-GW) je prvek jádra sítě definovaný ve specifikacích 3GPP, který usnadňuje doručování služby krátkých textových zpráv ([SMS](/mobilnisite/slovnik/sms/)) přes IP přístupové sítě. Jeho hlavní úlohou je fungovat jako zprostředkovatel a převodník protokolů mezi zastaralou SMS infrastrukturou, která je založena na signalizaci s přepojováním okruhů ([MAP](/mobilnisite/slovnik/map/) přes [SS7](/mobilnisite/slovnik/ss7/)), a uživatelským zařízením (UE) připojeným přes IP. Brána se vůči zastaralé síti prezentuje jako Mobile Switching Center/Visitor Location Register ([MSC](/mobilnisite/slovnik/msc/)/[VLR](/mobilnisite/slovnik/vlr/)) nebo Short Message Service Center ([SMSC](/mobilnisite/slovnik/smsc/)), zatímco vůči UE poskytuje rozhraní založené na IP (typicky využívající [SIP](/mobilnisite/slovnik/sip/) protokoly jako součást IMS).

Z architektonického hlediska je IP-SM-GW často integrována nebo úzce spojena s IP Multimedia Subsystem (IMS). Implementuje funkcionalitu definovanou v 3GPP TS 23.204 a TS 24.341. Když je UE registrováno pouze přes IP (např. přes VoLTE, VoWiFi nebo datové připojení), IP-SM-GW zaregistruje IP adresu a [MSISDN](/mobilnisite/slovnik/msisdn/) uživatele v Home Subscriber Server (HSS) jako aktuální obsluhující uzel pro SMS. Pro Mobile-Terminated (MT) SMS směruje SMSC zprávu na IP-SM-GW na základě této informace v HSS. IP-SM-GW poté převede MAP zprávu na SIP MESSAGE požadavek a doručí ji UE přes IP cestu (např. přes IMS Core).

Pro Mobile-Originated (MO) SMS je proces opačný. UE odešle SIP MESSAGE obsahující SMS datovou část na IP-SM-GW přes IMS. IP-SM-GW extrahuje obsah, naformátuje jej do standardní MAP zprávy a přepošle ji SMSC pro doručení příjemci. Brána zvládá základní funkce jako doručovací hlášení, převod mezi SIP a MAP stavovými kódy a správu viditelnosti účastníka (skrytí IP povahy doručení před zastaralým SMSC). Podporuje také SMS přes non-3GPP přístup (jako WLAN) a je klíčovou komponentou pro umožnění služby SMS v sítích, které nasadily Circuit-Switched Fallback (CSFB), nebo kde je rádiový přístup pouze LTE (bez domény s přepojováním okruhů).

## K čemu slouží

IP-SM-GW byla vytvořena k vyřešení kritického problému kontinuity služeb během přechodu od architektur s přepojováním okruhů (2G/3G) k plně IP architekturám (4G/5G). SMS je všudypřítomná, spolehlivá a velmi výnosná služba. Raná nasazení LTE (před VoLTE) byla pouze datová (s přepojováním paketů) a neměla nativní doménu s přepojováním okruhů pro přenos hovorů nebo SMS. Bez řešení by zařízení LTE přišla o schopnost SMS, což bylo pro uživatele a operátory nepřijatelné.

Počáteční provizorní řešení jako Circuit-Switched Fallback (CSFB) pro SMS nutila zařízení dočasně přepínat na 2G/3G síť pro odesílání/příjem zpráv, což způsobovalo zpoždění a signalizační zátěž. IP-SM-GW poskytla elegantnější, nativní IP řešení. Umožnila operátorům nabízet SMS jako IP aplikaci od prvního dne nasazení LTE, nezávisle na strategii hlasových služeb. To byl klíčový faktor pro raná LTE zařízení a datově orientované služby.

Navíc IP-SM-GW usnadnila zavedení služeb rich communication a VoLTE/VoWiFi tím, že zajistila dostupnost základní služby SMS přes stejné IP připojení používané pro hlas a data. Přemostila propast mezi starým a novým síťovým jádrem, chránila investice do zastaralé SMSC infrastruktury a zároveň umožnila vývoj služeb. Její vznik byl motivován potřebou zachovat životně důležitou službu, snížit závislost na zastaralých rádiových sítích a připravit cestu pro plně IP komunikaci.

## Klíčové vlastnosti

- Funguje jako funkce pro interoperabilitu protokolů mezi MAP/SS7 a SIP/IP
- Umožňuje doručování SMS přes LTE a další IP přístupy (např. WLAN)
- Registruje IP připojená UE v HSS pro účely směrování SMS
- Zpracovává jak Mobile-Originated, tak Mobile-Terminated SMS zprávy
- Generuje a překládá doručovací hlášení mezi IP a doménou s přepojováním okruhů
- Často je integrována s nebo připojena k IMS core pro přenos založený na SIP

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSFB – Circuit Switched Fallback](/mobilnisite/slovnik/csfb/)

## Definující specifikace

- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 29.338** (Rel-19) — Diameter protocols for SMS in MME/5GS
- **TS 29.577** (Rel-19) — IP-SM-GW & SMS Router SBI Protocol

---

📖 **Anglický originál a plná specifikace:** [IP-SM-GW na 3GPP Explorer](https://3gpp-explorer.com/glossary/ip-sm-gw/)
