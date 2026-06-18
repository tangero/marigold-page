---
slug: "smpp"
url: "/mobilnisite/slovnik/smpp/"
type: "slovnik"
title: "SMPP – Short Message Peer-to-Peer Protocol"
date: 2005-01-01
abbr: "SMPP"
fullName: "Short Message Peer-to-Peer Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/smpp/"
summary: "Short Message Peer-to-Peer Protocol (SMPP) je otevřený, průmyslový standardní protokol určený pro výměnu SMS zpráv mezi centry služby krátkých zpráv (SMSC) a externími zasílacími entitami, jako jsou E"
---

SMPP je otevřený, průmyslový standardní protokol pro výměnu SMS zpráv mezi centry služby krátkých zpráv (SMSC) a externími zasílacími entitami, který umožňuje hromadné SMS operace.

## Popis

Short Message Peer-to-Peer Protocol (SMPP) je protokol telekomunikačního průmyslu pracující na aplikační vrstvě, primárně používaný pro přenos dat krátkých zpráv mezi centrem služby krátkých zpráv ([SMSC](/mobilnisite/slovnik/smsc/)) a externí entitou pro krátké zprávy (ESME). ESME může být různorodá aplikace, například webový server, e-mailová brána nebo jiná platforma pro zasílání zpráv, která potřebuje odesílat nebo přijímat [SMS](/mobilnisite/slovnik/sms/). SMPP používá model klient-server, kde ESME typicky vystupuje jako SMPP klient (vysílač, přijímač nebo transceiver), který naváže trvalé [TCP/IP](/mobilnisite/slovnik/tcp-ip/) nebo X.25 spojení s SMSC, jež funguje jako SMPP server. Protokol definuje sadu operací komunikovaných prostřednictvím jednotek protokolových dat ([PDU](/mobilnisite/slovnik/pdu/)), které umožňují správu relace, odesílání zpráv, jejich doručování a dotazovací operace.

Protokol funguje prostřednictvím série bind operací (bind_transmitter, bind_receiver, bind_transceiver), které autentizují ESME a definují její roli. Po navázání spojení může ESME odesílat zprávy do SMSC k doručení pomocí PDU submit_sm, která obsahuje parametry jako zdrojová adresa (ton, npi), cílová adresa, schéma kódování dat a obsah zprávy (buď standardní 7bitová GSM abeceda, 8bitová data nebo [UCS-2](/mobilnisite/slovnik/ucs-2/) pro Unicode). Pro příjem zpráv SMSC doručí zprávy určené pro ESME pomocí PDU deliver_sm. SMPP také podporuje pokročilé funkce, jako je nahrazení zprávy, vícečástěné (zřetězené) zprávy prostřednictvím [UDH](/mobilnisite/slovnik/udh/) (User Data Header) a volitelné parametry ([TLV](/mobilnisite/slovnik/tlv/)) pro rozšířenou funkcionalitu. Protokol zahrnuje mechanismy řízení toku a vyžaduje pravidelné keep-alive zprávy (enquire_link) k udržení relace.

Architektura SMPP je vysoce efektivní pro scénáře hromadného zasílání. Podporuje synchronní i asynchronní režimy komunikace. V synchronním režimu žádost (request PDU) očekává odpovídající odpověď (response PDU). Asynchronní režim umožňuje nevyžádané PDU, jako jsou potvrzení o doručení (která jsou přenášena pomocí PDU deliver_sm s nastaveným specifickým esm_class) nebo výstrahy ze SMSC. Binární povaha protokolu a jeho relace orientovaný design minimalizují režii, což jej činí vhodným pro prostředí s vysokou propustností. Přestože byl původně vyvinut společností Aldiscon (později Logica, nyní součást Mobileum) a následně široce přijat, jeho popisy a pokyny pro použití byly zahrnuty do specifikací 3GPP (jako 23.040 a nyní stažená 23.039), aby byla zajištěna interoperabilita v ekosystému GSM/UMTS, nicméně zůstává průmyslovým standardem i mimo striktní hranice 3GPP.

## K čemu slouží

SMPP byl vytvořen, aby řešil rostoucí potřebu standardizovaného, efektivního a spolehlivého rozhraní mezi [SMSC](/mobilnisite/slovnik/smsc/) a rozšiřujícím se světem externích aplikací a poskytovatelů služeb. V počátcích SMS byly SMSC do značné míry uzavřené systémy s proprietárními rozhraními, což ztěžovalo a prodražovalo vývoj nadstavbových služeb (VAS) třetími stranami, jako jsou zpravodajská upozornění, bankovní notifikace nebo interaktivní hlasování. Toto omezení brzdilo inovace v ekosystému SMS. SMPP poskytl otevřený, dobře dokumentovaný protokol, který abstrahoval složitosti podkladové sítě a umožnil vývojářům aplikací soustředit se na logiku služby namísto integrace na nízké telekomunikační úrovni.

Historicky, jak využití SMS explodovalo mimo komunikaci mezi osobami, rostla poptávka po službách aplikace-osoba (A2P) a osoba-aplikace (P2A). Operátoři potřebovali způsob, jak bezpečně a škálovatelně připojit svá SMSC k externím entitám, jako jsou agregátoři obsahu, podnikové systémy a internetové brány. SMPP to vyřešil definováním jasného modelu klient-server s robustní autentizací, podporou transakcí s vysokým objemem a funkcemi nezbytnými pro komerční služby, jako jsou potvrzení o doručení, která jsou klíčová pro fakturaci a zajištění služeb. Jeho přijetí hlavními výrobci SMSC z něj učinilo de facto standard pro rozhraní SMS bran.

Protokol také řešil technická omezení dřívějších metod, jako bylo použití jednoduchých modemových AT příkazů nebo proprietárních binárních protokolů, které nebyly škálovatelné, postrádaly pokročilé funkce a trpěly problémy s interoperabilitou. Tím, že poskytl relace orientovaný, spojení založený protokol nad spolehlivými transportními vrstvami (TCP/IP), SMPP zajistil integritu zpráv, umožnil řízení toku a podpořil obousměrnou komunikaci potřebnou pro odesílání i přijímání zpráv. Jeho flexibilita v podpoře různých kódování dat a volitelných parametrů mu umožnila vyvíjet se spolu s technologií SMS, podporovat funkce jako zřetězené zprávy, flash SMS a indikátory WAP push, čímž zajistila budoucí použitelnost investic do infrastruktury pro zasílání zpráv.

## Klíčové vlastnosti

- Otevřený, binární protokol pro vysoce efektivní výměnu SMS přes TCP/IP nebo X.25
- Podpora více rolí ESME: Vysílač (Transmitter), Přijímač (Receiver) a Transceiver
- Komplexní sada PDU pro správu relace, odesílání zpráv, jejich doručování a dotazování
- Nativní podpora potvrzení o doručení a nahrazení zprávy
- Zpracovává zřetězené (dlouhé) SMS prostřednictvím parametrů hlavičky uživatelských dat (UDH)
- Rozšiřitelný pomocí volitelných parametrů (TLV) pro data specifická pro dodavatele

## Související pojmy

- [SMSC – Short Message Service Centre](/mobilnisite/slovnik/smsc/)
- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [UDH – User Data Header](/mobilnisite/slovnik/udh/)

## Definující specifikace

- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition

---

📖 **Anglický originál a plná specifikace:** [SMPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/smpp/)
