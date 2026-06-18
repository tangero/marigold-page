---
slug: "jsvm"
url: "/mobilnisite/slovnik/jsvm/"
type: "slovnik"
title: "JSVM – Joint Scalable Video Model"
date: 2025-01-01
abbr: "JSVM"
fullName: "Joint Scalable Video Model"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/jsvm/"
summary: "JSVM je referenční softwarový model pro rozšíření Scalable Video Coding (SVC) standardu H.264/AVC. V rámci 3GPP poskytuje standardizovanou implementaci pro testování a vývoj služeb škálovatelného vide"
---

JSVM je referenční softwarový model 3GPP pro rozšíření Scalable Video Coding (SVC) standardu H.264/AVC, poskytující standardizovanou implementaci pro vývoj a testování služeb škálovatelného videa.

## Popis

Joint Scalable Video Model (JSVM) je referenční softwarová implementace dodatku Scalable Video Coding ([SVC](/mobilnisite/slovnik/svc/)) ke standardu H.264/[AVC](/mobilnisite/slovnik/avc/) (MPEG-4 Part 10), vyvinutá společně skupinami [ITU-T](/mobilnisite/slovnik/itu-t/) VCEG a [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) [MPEG](/mobilnisite/slovnik/mpeg/). V rámci 3GPP je specifikován jako nástroj pro testování shody, ověřování interoperability a vývoj služeb škálovatelného videa. Funguje tak, že zakóduje video do základní vrstvy a jedné či více zlepšujících vrstev, což umožňuje časovou, prostorovou a kvalitativní ([SNR](/mobilnisite/slovnik/snr/)) škálovatelnost. Mezi klíčové komponenty patří softwarová sada JSVM obsahující nástroje enkodéru, dekodéru a extraktoru bitového toku, které implementují syntaxi a dekódovací procesy SVC. Architektura podporuje extrakci dílčích bitových toků tak, aby odpovídaly konkrétním požadavkům na šířku pásma, rozlišení nebo výpočetní výkon. Jeho úloha v 3GPP spočívá v poskytnutí normativní reference pro zajištění toho, aby implementace SVC pro služby jako Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a paketový streaming byly v souladu se standardem, což garantuje interoperabilitu napříč sítěmi a zařízeními.

## K čemu slouží

JSVM byl vytvořen k řešení výzvy efektivního doručování videa přes heterogenní sítě různorodým zařízením s odlišnými možnostmi. Předchozí neškálovatelné kódování videa vyžadovalo více zakódovaných verzí (transkódování) stejného obsahu, což zvyšovalo nároky na úložiště a složitost. SVC prostřednictvím reference JSVM tento problém řeší tím, že umožňuje adaptaci jediného zakódovaného bitového toku dynamicky. To je klíčové pro mobilní prostředí, kde se šířka pásma a možnosti koncového zařízení liší, což umožňuje plynulé snižování kvality a efektivní multicast/broadcast. Historickým kontextem je snaha o pokročilé mobilní TV a streamovací služby ve specifikacích 3GPP Releases 7-9, kde bylo škálovatelné video považováno za klíčové pro MBMS a adaptivní HTTP streaming.

## Klíčové vlastnosti

- Referenční implementace H.264/SVC (Scalable Video Coding)
- Podporuje prostorové, časové a kvalitativní (SNR) škálovatelné vrstvy
- Obsahuje nástroje enkodéru, dekodéru a extrakce bitového toku pro testování
- Umožňuje adaptivní doručování videa extrakcí dílčích bitových toků
- Používá se pro testování shody a interoperability v 3GPP
- Usnadňuje efektivní multicast/broadcast (MBMS) a unicast streaming

## Související pojmy

- [SVC – Switched Virtual Circuit](/mobilnisite/slovnik/svc/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TR 26.904** (Rel-19) — Future video capability requirements for streaming and MBMS

---

📖 **Anglický originál a plná specifikace:** [JSVM na 3GPP Explorer](https://3gpp-explorer.com/glossary/jsvm/)
