---
slug: "pbs"
url: "/mobilnisite/slovnik/pbs/"
type: "slovnik"
title: "PBS – Personal Broadcast Service"
date: 2025-01-01
abbr: "PBS"
fullName: "Personal Broadcast Service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pbs/"
summary: "Služba 3GPP, která umožňuje uživateli vysílat multimediální obsah z osobního zařízení definované skupině příjemců přes mobilní síť. Umožňuje sdílení typu jeden k mnoha živého nebo nahraného média, jak"
---

PBS je služba 3GPP, která umožňuje uživateli vysílat multimediální obsah z osobního zařízení definované skupině přes mobilní síť, přičemž pro sdílení typu jeden k mnoha využívá doručování pomocí MBMS nebo unicastu.

## Popis

Personal Broadcast Service (PBS) je standardizovaná služební funkce definovaná 3GPP, která umožňuje jednotlivému uživateli vystupovat jako zdroj vysílání a distribuovat audio, video nebo datový obsah ze svého uživatelského zařízení (UE) potenciálně velké, předem definované skupině jiných uživatelů. Služba je navržena tak, aby využívala stávající možnosti vysílání/multicastu 3GPP, především službu Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), ale může také využít doručování unicastem pro menší skupiny nebo záložní scénáře. Zapojené funkce jádra sítě zahrnují Broadcast-Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) pro oznámení služby, plánování a doručování obsahu spolu se standardními prvky 5G Core (5GC) nebo Evolved Packet Core (EPC) pro správu uživatelů a relací.

Jak PBS funguje, začíná poskytováním služby a správou skupiny. Uživatel, vysílatel, zahájí relaci prostřednictvím klientské aplikace. Síť uživatele ověří a autorizuje vysílání na základě profilů předplatného. Služba může být předem naplánována nebo zahájena ad-hoc. Pro doručování založené na MBMS přijímá BM-SC mediální stream z UE vysílatele (často přes unicastový uplink), který pak replikuje a doručuje pomocí přenosů MBMS přes Radio Access Network (RAN) všem přihlášeným příjemcům v konkrétní servisní oblasti. RAN využívá pro efektivní přenos stejného obsahu k více UE současně operaci Single Frequency Network ([MBSFN](/mobilnisite/slovnik/mbsfn/)) v LTE nebo službu NR Multicast and Broadcast Service ([MBS](/mobilnisite/slovnik/mbs/)) v 5G, čímž šetří rádiové prostředky.

Role PBS v síti spočívá v poskytování škálovatelného, pro síť efektivního mechanismu pro sdílení osobního obsahu, který přesahuje komunikaci jeden k jednomu. Nachází se na průsečíku tradičních buněčných služeb a aplikací sociálních médií/vysílání. Mezi klíčové technické aspekty patří dynamická správa skupin, objevování služeb (např. pomocí mechanismů jako MBMS User Service Discovery), zabezpečení pro šifrování obsahu a řízení přístupu ke skupině a modely účtování. Síť musí zvládnout asymetrii služby: vysokokapacitní uplink od jediného vysílatele a efektivní downlinkovou distribuci k mnoha divákům, optimalizující využití prostředků zejména při živých událostech, kdy mnoho uživatelů ve stejné geografické oblasti chce přijímat stejný stream.

## K čemu slouží

PBS byla vytvořena, aby reagovala na rostoucí poptávku uživatelů po sdílení živých zážitků – jako jsou události, osobní okamžiky nebo profesní prezentace – s vybranou skupinou v reálném čase přímo z mobilního zařízení. Před její standardizací byla tato funkcionalita primárně nabízena aplikacemi Over-The-Top ([OTT](/mobilnisite/slovnik/ott/)) využívajícími pro každého diváka unicastová spojení, což je pro síť při růstu publika v lokalizované oblasti vysoce neefektivní. Tento unicastový přístup spotřebovává nadměrné rádiové a jádrové síťové prostředky, protože stejné datové pakety jsou přenášeny vícekrát přes stejnou buňku.

Služba řeší problém škálovatelné a efektivní osobní komunikace typu jeden k mnoha. Tím, že využívá inherentní efektivitu vysílacích/multicastových technologií jako je [MBMS](/mobilnisite/slovnik/mbms/), umožňuje PBS síti přenášet jediný datový stream, který mohou přijímat všichni zainteresovaní uživatelé v rámci buňky nebo servisní oblasti. To dramaticky snižuje zatížení RAN a jádra sítě ve srovnání s replikovanými unicastovými streamy. Její vznik byl motivován konvergencí trendů sociálního vysílání a možností buněčných sítí, což poskytuje operátorům standardizovanou, pro síť optimalizovanou služební platformu pro konkurenci s nabídkami OTT a umožňuje nové zdroje příjmů v oblastech jako živé sociální video, aktualizace mikrokomerčních komunit a podniková komunikace.

## Klíčové vlastnosti

- Umožňuje jednomu UE zahájit vysílací/multicastovou relaci pro definovanou skupinu
- Využívá 3GPP MBMS/MBS pro efektivní využití rádiových prostředků v downlinku
- Podporuje jak předem naplánované, tak ad-hoc (živé) vysílací relace
- Zahrnuje mechanismy pro správu skupin, předplatné a objevování služeb
- Poskytuje rámce pro účtování a zabezpečení pro řízení přístupu a ochranu obsahu
- Může využít doručování unicastem jako záložní řešení nebo pro scénáře s malými skupinami

## Definující specifikace

- **TR 22.947** (Rel-19) — Personal Broadcast Service (PBS) Use Cases

---

📖 **Anglický originál a plná specifikace:** [PBS na 3GPP Explorer](https://3gpp-explorer.com/glossary/pbs/)
