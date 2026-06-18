---
slug: "ptzf"
url: "/mobilnisite/slovnik/ptzf/"
type: "slovnik"
title: "PTZF – Pan, Tilt, Zoom, and Focus"
date: 2025-01-01
abbr: "PTZF"
fullName: "Pan, Tilt, Zoom, and Focus"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ptzf/"
summary: "Sada parametrů ovládání kamery standardizovaná pro dálkový provoz v multimediálních službách. Umožňuje síťové řízení orientace kamery (pan/tilt), přiblížení (zoom) a zaostření objektivu, což je klíčov"
---

PTZF je standardizovaná sada parametrů ovládání kamery pro dálkový provoz, umožňující síťové řízení horizontálního a vertikálního natočení (pan/tilt), přiblížení (zoom) a zaostření (focus) kamery v multimediálních službách.

## Popis

PTZF označuje standardizované řízení čtyř základních mechanických funkcí kamery: horizontálního otáčení (Pan), vertikálního otáčení (Tilt), optického nebo digitálního přiblížení (Zoom) a zaostření objektivu (Focus). V kontextu 3GPP je tato funkce definována v rámci architektury služby Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a mediálního streamování, konkrétně pro aplikace vyžadující dálkové ovládání kamery. Standardizace zajišťuje interoperabilní signalizaci řízení mezi klientskou aplikací (ovladačem) a mediálním serverem nebo koncovým zařízením s kamerou (řízeným zařízením).

Z architektonického hlediska je ovládání PTZF typicky zprostředkováno prostřednictvím protokolu pro řízení médií, často integrovaného v rámci protokolů pro správu relací, jako je [RTSP](/mobilnisite/slovnik/rtsp/) (Real Time Streaming Protocol), nebo prostřednictvím vyhrazených rozhraní [API](/mobilnisite/slovnik/api/) na mediálním serveru. Specifikace 3GPP, zejména TS 26.114 pro zpracování médií založené na IP Multimedia Subsystem (IMS), poskytují rámec pro přenos PTZF příkazů jako součást mediální relace. Řídicí příkazy jsou generovány uživatelským rozhraním na straně klienta, zabaleny do standardizovaných zpráv a přenášeny přes síť k řídicí jednotce kamerového systému.

Princip fungování zahrnuje kontinuální zpětnovazební smyčku. Klient odesílá požadavky na řízení (např. 'otočit vlevo o 30 stupňů', 'přiblížit 2x'). Tyto požadavky jsou přenášeny v datové části zpráv řídicího protokolu. Příjemce – mediální procesor nebo řídicí jednotka kamery – tyto příkazy interpretuje a podle toho aktivuje fyzické mechanismy kamery. Pro plynulý uživatelský zážitek je následně mediální proud (video) z kamery kódován a přenášen zpět ke klientovi, často s využitím adaptivního streamování s proměnným datovým tokem, takže uživatel vidí výsledky svých PTZF akcí téměř v reálném čase. Mezi klíčové komponenty patří kamera s podporou PTZF, mediální server přenášející řídicí signály a média a klientský přehrávač s ovládacím rozhraním.

Její úloha v síti spočívá v umožnění bohatých, interaktivních mediálních služeb přesahujících pouhé pasivní sledování. Mění jednosměrný video přenos v interaktivní relaci. To je zásadní pro aplikace jako je dálkový dohled, kde operátor může prohledávat oblast, pro živé přenosy událostí, kde režisér může volit záběry, nebo pro imerzivní zážitky jako virtuální pohledy ze stadionu. Standardizací těchto ovládacích prvků 3GPP zajišťuje, že poskytovatelé služeb mohou nasazovat interoperabilní řešení a výrobci zařízení mohou vyrábět kompatibilní zařízení, čímž podporují ekosystém pokročilých multimediálních služeb v mobilních sítích.

## K čemu slouží

Standardizace PTZF byla motivována rostoucím trhem interaktivních a dálkově ovládaných video služeb přes IP sítě, včetně mobilních sítí. Před standardizací existovala proprietární řešení pro dálkové ovládání kamer, ta však vedla k závislosti na konkrétním dodavateli, bránila interoperabilitě služeb a komplikovala integraci různých kamer, serverů a klientských aplikací do jedné nabídky služeb.

Základním problémem, který PTZF řeší, je absence univerzálního 'jazyka' pro základní ovládání kamery v síťových multimediálních systémech. Bez něj by systém dohledu od dodavatele A nemohl být ovládán klientskou aplikací od dodavatele B, což by omezovalo volbu a inovace. Standardizace prostřednictvím 3GPP umožňuje poskytovatelům služeb budovat platformy, které mohou pracovat s kamerami od více výrobců a nabízet služby široké škále klientských zařízení.

Historicky se tato potřeba stala naléhavou s nástupem IMS a vize obohacených komunikačních služeb. Aplikace jako multimediální telefonie, videokonference a vysílání obsahu vyžadovaly více než jen statický video přenos. Schopnost uživatele nebo automatizovaného systému řídit pozorovací perspektivu byla vnímána jako klíčová přidaná hodnota. Definováním PTZF v rovině řízení médií poskytlo 3GPP základní schopnost pro novou třídu interaktivních mediálních služeb, podporujících případy užití od osobních videohovorů po profesionální mediální produkci a veřejnou bezpečnost.

## Klíčové vlastnosti

- Standardizovaná signalizace řízení pro orientaci kamery (pan a tilt)
- Standardizované řízení úrovní optického/digitálního přiblížení (zoom)
- Standardizované řízení nastavení zaostření objektivu kamery (focus)
- Definováno v rámci frameworků pro zpracování médií v IMS a MBMS
- Umožňuje interoperabilní dálkové ovládání kamery napříč dodavateli
- Podporuje služby interaktivního videa a dohledu v reálném čase

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [RTSP – Real-time Streaming Protocol](/mobilnisite/slovnik/rtsp/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling

---

📖 **Anglický originál a plná specifikace:** [PTZF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ptzf/)
