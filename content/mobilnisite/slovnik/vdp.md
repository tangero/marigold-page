---
slug: "vdp"
url: "/mobilnisite/slovnik/vdp/"
type: "slovnik"
title: "VDP – Viewport Dependent Processing"
date: 2025-01-01
abbr: "VDP"
fullName: "Viewport Dependent Processing"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vdp/"
summary: "Technika zpracování médií pro imerzivní video služby, jako je VR/360° video. Optimalizuje kódování a doručování tím, že soustředí vysoce kvalitní zdroje pouze na aktuální zorné pole uživatele (viewpor"
---

VDP je technika zpracování médií pro imerzivní video, která optimalizuje kódování tím, že soustředí vysoce kvalitní zdroje pouze na aktuální uživatelův výřez (viewport), čímž snižuje potřebu šířky pásma.

## Popis

Viewport Dependent Processing (VDP) je klíčová technika definovaná 3GPP pro efektivní doručování imerzivních médií, jako je virtuální realita ([VR](/mobilnisite/slovnik/vr/)) a video 360°, přes mobilní sítě. Funguje na principu, že uživatel konzumující sférické video vidí v daném okamžiku pouze část celé scény 360° – tato viditelná část je výřez (viewport). VDP dynamicky přizpůsobuje kódování a doručování médií tak, aby upřednostnilo vysokou kvalitu pro předpovězenou nebo požadovanou oblast výřezu, zatímco snižuje kvalitu nebo rozlišení oblastí mimo výřez. Tato prostorová diferenciace kvality je klíčová, protože přenos celého sférického videa ve stejně vysoké kvalitě by vyžadoval nepřiměřeně vysokou šířku pásma, což by vedlo k bufferingu a špatnému uživatelskému zážitku na omezených bezdrátových spojích.

Architektura pro VDP zahrnuje úzkou interakci mezi mediálním serverem, klientskou aplikací a doručovací sítí. Mediální server typicky ukládá nebo generuje více zakódovaných reprezentací (dlaždic nebo oblastí) videa 360°. Klient, často VR headset nebo smartphone v head-mounted displeji, sleduje orientaci hlavy uživatele (odchylku, náklon a někdy i rotaci) a tuto informaci o výřezu periodicky hlásí zpět serveru nebo síťovému zprostředkovateli. Na základě této zpětné vazby a potenciálně s využitím predikčních algoritmů výřezu systém určí, které video dlaždice nebo vrstvy kvality odpovídající aktuálnímu a předpovězenému budoucímu výřezu je třeba doručit s vysokou prioritou. Doručování může být řízeno pomocí protokolů adaptivního streamování s proměnnou datovou rychlostí, jako je [DASH](/mobilnisite/slovnik/dash/), kde je Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)) strukturována tak, aby popsala tyto prostorově diferencované kvalitní reprezentace.

Klíčové komponenty v ekosystému VDP zahrnují mediálního klienta sledujícího výřez, mediální server nebo kodér podporující VDP a framework 5G Media Streaming ([5GMS](/mobilnisite/slovnik/5gms/)), který poskytuje [API](/mobilnisite/slovnik/api/) a funkce pro orchestraci. Technika spoléhá na efektivní dlaždicové kódování, kde je snímek videa 360° rozdělen na mřížku nezávisle dekódovatelných segmentů. To umožňuje klientovi vyžádat a dekódovat pouze dlaždice uvnitř výřezu ve vysoké kvalitě a složit je pro zobrazení. Úlohou VDP v síti je fungovat jako inteligentní adaptační vrstva médií, která překládá záměr uživatelské imerze do efektivního využití síťových zdrojů, což umožňuje vysoce kvalitní VR zážitky přes 5G bez zahlcení rádiového přístupu a jádra sítě zbytečnými daty.

## K čemu slouží

VDP bylo zavedeno, aby vyřešilo základní problém šířky pásma při doručování imerzivního videa přes mobilní sítě. Před jeho standardizací vyžadovalo doručování videa 360° nebo [VR](/mobilnisite/slovnik/vr/) streamování celé sférické scény v kvalitě dostatečné pro jakýkoli potenciální výřez, což vedlo k datovým rychlostem často přesahujícím 100 Mbps pro obsah s vysokým rozlišením a vysokou snímkovou frekvencí. To bylo pro hromadnou mobilní spotřebu nepraktické, způsobovalo nadměrnou latenci, buffering a rychlé vybíjení baterie v uživatelském zařízení. Omezení monolitického přístupu ke streamování, který nebere v úvahu výřez, vážně bránilo komerční životaschopnosti služeb mobilní VR.

Vytvoření VDP v 3GPP Release 17 bylo motivováno snahou průmyslu směrem k metaversu a vylepšeným zážitkům z mobilních médií v rámci ekosystému 5G. Řeší tento problém sladěním doručování médií s lidským vnímáním – neplýtvá bity na části scény, které uživatel nevidí. Tento posun paradigmatu od jednotného streamování k streamování optimalizovanému pro výřez snižuje potřebnou šířku pásma až o 80 % při stejné vnímané vizuální kvalitě, což činí streamování VR s vysokou věrností proveditelným přes pokročilé 5G sítě. Umožňuje nové servisní modely pro operátory a poskytovatele obsahu, čímž mění imerzivní média z okrajové, připojené aplikace na škálovatelnou službu vhodnou pro mobilní použití.

## Klíčové vlastnosti

- Prostorová adaptace kvality na základě sledování výřezu v reálném čase
- Dlaždicové kódování pro nezávislé vyžádání a dekódování oblastí výřezu
- Integrace s MPEG-DASH pro dynamické adaptivní streamování přes HTTP
- Predikce výřezu pro přednačtení obsahu a zmírnění latence mezi pohybem a fotony
- Podpora v rámci aplikačního frameworku 5G Media Streaming (5GMS)
- Snížení potřebné šířky pásma až o 80 % ve srovnání se streamováním nezávislým na výřezu

## Související pojmy

- [5GMS – 5G Media Streaming](/mobilnisite/slovnik/5gms/)
- [VR – Virtualized Resource](/mobilnisite/slovnik/vr/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.962** (Rel-19) — ITT4RT Operation and Usage Guidelines

---

📖 **Anglický originál a plná specifikace:** [VDP na 3GPP Explorer](https://3gpp-explorer.com/glossary/vdp/)
