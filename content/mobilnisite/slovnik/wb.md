---
slug: "wb"
url: "/mobilnisite/slovnik/wb/"
type: "slovnik"
title: "WB – Wideband"
date: 2025-01-01
abbr: "WB"
fullName: "Wideband"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/wb/"
summary: "WB označuje širokopásmový (wideband) přenos zvuku, typicky s šířkou pásma 50–7000 Hz, používaný v řečových kodecích jako AMR-WB, který poskytuje výrazně vyšší kvalitu a přirozenost řeči ve srovnání s"
---

WB je širokopásmová (wideband) audio technologie, typicky využívající šířku pásma 50–7000 Hz, která zlepšuje kvalitu a přirozenost řeči ve službách 3GPP, jako je VoLTE, prostřednictvím kodeků jako je AMR-WB.

## Popis

V kontextu 3GPP termín Wideband (WB) konkrétně označuje přenos zvuku v kmitočtovém pásmu 50–7000 Hz, což je podstatné rozšíření oproti tradičnímu úzkopásmovému ([NB](/mobilnisite/slovnik/nb/)) telefonnímu pásmu 300–3400 Hz. Tato širší šířka pásma je implementována prostřednictvím kodeků, jako je Adaptive Multi-Rate Wideband ([AMR-WB](/mobilnisite/slovnik/amr-wb/)), který byl v 3GPP standardizován jako první širokopásmový řečový kodek. Technická implementace zahrnuje vzorkování řeči na 16 kHz, což umožňuje zachytit a reprodukovat mnohem bohatší škálu kmitočtů, zejména nízkých basových tónů a vyšších harmonických složek, které přispívají k identifikaci mluvčího a přirozenému zvuku.

Architektura pro integraci WB hlasových služeb zahrnuje více síťových komponent. UE musí podporovat WB kodek (např. AMR-WB) a jádro sítě, konkrétně IP Multimedia Subsystem (IMS) pro VoLTE/VoNR, musí při navazování relace pomocí protokolů [SIP](/mobilnisite/slovnik/sip/)/[SDP](/mobilnisite/slovnik/sdp/) vyjednat a podporovat WB kodek. Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) může také podporovat WB pro konferenční hovory a hlasové zprávy. Klíčem k fungování je end-to-end vyjednání kodeku; pokud oba koncové body a síťová cesta WB podporují, je navázán WB hovor. V opačném případě systém přejde na úzkopásmový režim (fallback). Úlohou WB v síti je zvýšit kvalitu uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)) u hlasových služeb, díky čemuž konverzace zní přirozeněji a jsou méně únavné, což je klíčový diferenciátor služeb operátorů.

Provoz WB se řídí specifickými přenosovými rychlostmi definovanými pro kodek. U AMR-WB se pohybují od 6,60 kbit/s do 23,85 kbit/s v devíti módech. Kodek přizpůsobuje svou přenosovou rychlost na základě síťových podmínek (např. dostupné šířky pásma, chybovosti) při zachování širokého kmitočtového pásma. Tato adaptabilita je klíčovou vlastností zajišťující robustnost. Zavedení WB hlasu bylo významným milníkem ve vývoji od okruhově přepínaných hlasových služeb k paketově přepínanému Voice over LTE (VoLTE), kde bylo možné vylepšený kodek snáze integrovat a stal se standardní funkcí pro vysokokvalitní hlasové hovory.

## K čemu slouží

Technologie WB byla vytvořena, aby vyřešila dlouhodobý problém špatné, „plechové“ kvality hlasu v tradiční telefonii, která byla omezena úzkým pásmem 3,1 kHz v [PSTN](/mobilnisite/slovnik/pstn/) a raných mobilních systémech. Toto úzkopásmové filtrování, původně navržené pro efektivitu měděných vedení, odstraňovalo kritické nízké a vysoké kmitočty, což snižovalo přirozenost řeči, způsobovalo únavu posluchače a ztěžovalo rozpoznání mluvčího. Motivací pro WB bylo využít zvýšenou šířku pásma a paketově orientovanou povahu sítí 3G a později 4G/5G k dosažení kvality hlasové služby srovnatelné nebo lepší než u [FM](/mobilnisite/slovnik/fm/) rádia nebo osobního rozhovoru.

Historický kontext zahrnuje standardizaci AMR-WB (G.722.2) nejprve v ITU-T v roce 2002 a jeho následné přijetí v 3GPP Release 5. Jeho integrace do sítí 3GPP řešila omezení stávajícího kodeku AMR-NB a poskytla jasnou evoluční cestu pro kvalitu hlasu. Hnacím motorem byla konkurenční diferenciace pro operátory a naplnění uživatelských očekávání ohledně multimediální kvality ve světě stále více orientovaném na data. WB hlas se stal základním kamenem služby VoLTE, což operátorům umožnilo nabízet HD Voice jako prémiovou službu, která příčně řeší kvalitativní propast oproti OTT hlasovým aplikacím a stanovuje novou základní úroveň pro mobilní hlas.

## Klíčové vlastnosti

- Kmitočtové pásmo 50–7000 Hz (oproti 300–3400 Hz u NB)
- Implementace prostřednictvím kodeků jako je AMR-WB (G.722.2)
- Vzorkovací kmitočet 16 kHz
- Více adaptivních přenosových rychlostí (např. 6,6 až 23,85 kbit/s pro AMR-WB)
- End-to-end vyjednání prostřednictvím IMS/SIP pro VoLTE/VoNR
- Vylepšená přirozenost řeči a komfort pro posluchače

## Související pojmy

- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TS 26.103** (Rel-19) — 3GPP Codec Lists for OoBTC and TrFO
- **TR 26.921** (Rel-19) — UE Performance in Ambient Noise
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.522** (Rel-19) — 5G NEF Northbound APIs Stage 3

---

📖 **Anglický originál a plná specifikace:** [WB na 3GPP Explorer](https://3gpp-explorer.com/glossary/wb/)
