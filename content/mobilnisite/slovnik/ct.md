---
slug: "ct"
url: "/mobilnisite/slovnik/ct/"
type: "slovnik"
title: "CT – Call Transfer supplementary service"
date: 2025-01-01
abbr: "CT"
fullName: "Call Transfer supplementary service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ct/"
summary: "CT je doplňková služba v sítích 3GPP, která umožňuje uživateli převést probíhající hovor na třetí stranu. Umožňuje přenášející straně buď hovor převzít zpět, nebo přenos dokončit, čímž usnadňuje správ"
---

CT (Call Transfer) je doplňková služba v sítích 3GPP, která umožňuje uživateli převést probíhající hovor na třetí stranu.

## Popis

Call Transfer (CT) je standardizovaná doplňková služba definovaná v rámci architektury jádra sítě a služeb 3GPP. Funguje na aplikační vrstvě, interaguje s entitou Call Control ([CC](/mobilnisite/slovnik/cc/)) v okruhově spínané ([CS](/mobilnisite/slovnik/cs/)) doméně a je spravována Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) a Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo jádrem IP Multimedia Subsystem (IMS) pro novější verze. Servisní logika je prováděna v síťových uzlech, nikoli v uživatelském zařízení (UE), ačkoli UE poskytuje uživatelské rozhraní pro aktivaci a vyvolání služby.

Služba funguje prostřednictvím definované sekvence signalizačních zpráv mezi zúčastněnými stranami: stranou přenášející hovor (Uživatel A), původně volanou stranou (Uživatel B) a stranou, na kterou je hovor převeden (Uživatel C). Když Uživatel A během aktivního hovoru s Uživatelem B vyvolá CT, síť Uživatele B pozastaví a naváže nové spojení k Uživateli C. V závislosti na variantě přenosu může Uživatel A buď ze hovoru odejít (čímž přenos dokončí), nebo všechny strany spojit do konference. Mezi klíčové protokolové komponenty patří [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) nebo Bearer Independent Call Control (BICC) v CS jádru a metody Session Initiation Protocol (SIP) REFER v rámci IMS.

Z architektonického hlediska je služba zřízena v servisním profilu uživatele uloženém v HLR/Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Během registrace nebo navázání hovoru je tento profil stažen do obsluhujícího MSC nebo Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)). Skutečné provádění služby provádí MSC Server nebo Telephony Application Server (TAS) v prostředí IMS. Služba interaguje se základními modely stavu hovoru pro správu více hovorových větví a jejich asociací.

Její role v síti spočívá v obohacení základní telefonní nabídky služeb, což umožňuje sofistikované scénáře obsluhy hovorů nezbytné pro firemní i osobní použití. Je součástí sady doplňkových služeb, jako je Call Forwarding (CF) a Call Waiting (CW), které společně poskytují kompletní telefonní prostředí bohaté na funkce. V moderních sítích, zejména s VoLTE a VoNR, je CT implementována jako služba založená na IMS, což zajišťuje bezproblémový provoz napříč přístupovými technologiemi.

## K čemu slouží

CT byla vytvořena za účelem replikace a standardizace možností přenosu hovorů známých z tradičních pevných ústředen (PBX) a firemních telefonních systémů pro mobilní doménu. Před její standardizací v 3GPP nabízely mobilní sítě primárně pouze základní volání. Nedostatek pokročilých funkcí pro obsluhu hovorů omezoval užitečnost mobilních telefonů pro profesionální a kolaborativní případy užití, kde je běžným požadavkem převod hovoru na vhodnějšího kolegu nebo oddělení.

Problém, který řeší, je statická povaha dvoustranného hovoru. V mnoha situacích osoba, která hovor přijme, nemusí být správným koncovým bodem pro konverzaci. CT dynamicky přesměruje navázané hovorové sezení na třetí stranu, aniž by původně volaná strana musela zavěsit a volat znovu. Tím šetří čas, zlepšuje uživatelský zážitek a zvyšuje produktivitu usnadněním efektivního směrování hovorů v rámci organizací.

Historicky bylo její zavedení v Release 5 součástí širšího úsilí o to, aby se sítě GSM/UMTS staly funkčně konkurenceschopné vůči pevným službám ISDN. Řešila omezení starších mobilních systémů, kterým chyběly standardizované, na síti založené doplňkové služby. Poskytnutím jednotného mechanismu napříč různými síťovými operátory a výrobci terminálů CT zajistila interoperabilitu a konzistentní uživatelský zážitek, což bylo klíčové pro přijetí mobilních telefonů jako primárních obchodních nástrojů.

## Klíčové vlastnosti

- Umožňuje přenos aktivního hovoru na třetí stranu
- Podporuje varianty jako Explicit Call Transfer (ECT), kde přenášející strana přenos explicitně iniciuje
- Provádění služby je síťové, nezávislé na schopnostech terminálu
- Spolupracuje se základním řízením hovoru a dalšími doplňkovými službami
- Zřizování a předplatné řízeno prostřednictvím HLR/HSS
- Standardizované signalizační procedury pro spolehlivý provoz napříč zařízeními různých výrobců

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.826** (Rel-17) — Study on 5G for Critical Medical Applications
- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks

---

📖 **Anglický originál a plná specifikace:** [CT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ct/)
