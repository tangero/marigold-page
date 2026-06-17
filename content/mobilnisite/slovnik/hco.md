---
slug: "hco"
url: "/mobilnisite/slovnik/hco/"
type: "slovnik"
title: "HCO – Hear Carry Over"
date: 2025-01-01
abbr: "HCO"
fullName: "Hear Carry Over"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hco/"
summary: "HCO je funkce umožňující uživateli střídavě přijímat řeč a vysílat text, primárně pro služby zpřístupnění, jako je textová telefonie. Umožňuje plynulé přepínání mezi poslechem a psaním a usnadňuje kom"
---

HCO je funkce, která umožňuje uživateli střídavě přijímat řeč a vysílat text, primárně pro služby zpřístupnění, a usnadňuje tak komunikaci v reálném čase pro uživatele se sluchovým nebo řečovým postižením.

## Popis

Hear Carry Over (HCO) je servisní funkce standardizovaná 3GPP, která usnadňuje střídavý režim komunikace, kdy uživatel může přijímat hlasový zvuk a vysílat textová data sekvenčně nebo paralelně. Základní provozní princip spočívá v tom, že koncové zařízení (např. mobilní telefon nebo asistenční zařízení) spravuje dva odlišné mediální proudy: downlink hlasový kanál a uplink textový kanál. Uživatelské rozhraní a síťové protokoly koordinují, aby uživatel mohl naslouchat příchozí řeči a poté sestavit a odeslat textovou odpověď, čímž vzniká konverzační vzor střídání. To je často implementováno ve spojení se službami jako Total Conversation nebo textová telefonie (TTY) přes IP sítě, kde protokol RTP přenáší řeč a textové médium, případně s využitím formátů RTP payload pro text. Síťový IP Multimedia Subsystem (IMS) typicky poskytuje řízení služby, přičemž pro navázání relace a vyjednávání funkcí se používá protokol SIP. Terminál musí podporovat specifické kodeky a vyrovnávací mechanismy pro zvládnutí časování a synchronizace mezi audio a textovými proudy, aby konverzace působila přirozeně a byla responzivní. Z pohledu sítě vyžadují HCO relace odpovídající zpracování Quality of Service (QoS), protože proud řeči v reálném čase je citlivý na zpoždění, zatímco textový proud, ačkoli v reálném čase, může tolerovat mírně odlišné profily latence. Funkce je závislá na schopnosti podkladové paketové sítě podporovat souběžné mediální toky s různými charakteristikami, což je schopnost vlastní sítím LTE a 5G.

## K čemu slouží

HCO bylo zavedeno, aby řešilo potřebu přístupných telekomunikací pro jednotlivce se sluchovým nebo řečovým postižením. Před takovými standardizovanými funkcemi byly možnosti komunikace omezené, často závislé na samostatných, vyhrazených zařízeních pro textovou telefonii, která nebyla integrována do hlavních mobilních služeb. Motivací bylo využít schopnosti IP mobilních sítí (jako jsou ty definované od 3GPP Release 10 a dále) k poskytování integrovaných konverzačních služeb v reálném čase, které kombinují audio a text. Tím se řeší problém umožnění obousměrné komunikace, kdy jedna strana může primárně používat text a druhá řeč, což je běžný scénář v přepisovacích službách nebo přímých konverzacích mezi slyšícími a neslyšícími uživateli. Standardizací HCO zajistil 3GPP interoperabilitu mezi uživatelským zařízením a síťovými službami, což podpořilo široké přijetí a inkluzi. Řešilo to omezení předchozí textové telefonie v přepojovaných okruzích, která byla často pomalá, měla špatnou kvalitu zvuku a nebyla plynule integrována s moderními multimediálními službami. HCO jako součást souboru funkcí zpřístupnění umožňuje mobilním sítím plnit regulační a společenské povinnosti pro univerzální službu.

## Klíčové vlastnosti

- Střídavý příjem řeči a vysílání textu
- Podpora přenosu textu v reálném čase (RTT) přes IP
- Integrace s poskytováním služeb založeným na IMS
- Správa relací prostřednictvím vyjednávání SIP a SDP
- Využití RTP pro přenos média s odpovídajícími formáty payload
- Koordinace vyrovnávací paměti na terminálu a uživatelského rozhraní pro střídání

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 22.226** (Rel-19) — Global Text Telephony (GTT) Stage 1

---

📖 **Anglický originál a plná specifikace:** [HCO na 3GPP Explorer](https://3gpp-explorer.com/glossary/hco/)
