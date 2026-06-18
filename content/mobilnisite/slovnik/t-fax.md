---
slug: "t-fax"
url: "/mobilnisite/slovnik/t-fax/"
type: "slovnik"
title: "T-FAX – Transmission side facsimile"
date: 2025-01-01
abbr: "T-FAX"
fullName: "Transmission side facsimile"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/t-fax/"
summary: "T-FAX označuje funkci na straně vysílání pro služby faksimilního přenosu skupiny 3 (Group 3 facsimile) přes sítě 3GPP. Zahrnuje protokoly a procedury v síti (např. v MSC nebo IMS), které zajišťují ode"
---

T-FAX je funkce a protokoly na straně vysílání v síti 3GPP, které zajišťují odesílání faxových dat a interoperabilitu s tradičními faxovými přístroji a službami.

## Popis

Faksimilní přenos na straně vysílání (T-FAX) je termín 3GPP, který specifikuje síťové komponenty a procedury zodpovědné za přenos faksimilních dat v rámci mobilní sítě. Je součástí širší specifikace služeb faksimilního přenosu 3GPP, která zajišťuje zpětnou kompatibilitu s hojně rozšířeným standardem faksimilního přenosu skupiny 3 (G3) používaným ve veřejné telefonní síti ([PSTN](/mobilnisite/slovnik/pstn/)). V kontextu přepojování okruhů (např. GSM, UMTS) je funkce T-FAX typicky implementována v Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)). MSC funguje jako prostředník mezi mobilní stanicí (strana příjmu nebo ukončení) a PSTN nebo jiným faxovým terminálem.

Provoz zahrnuje několik klíčových fází. Nejprve během navazování hovoru MSC identifikuje hovor jako faksimilní relaci na základě informací o nosné službě. Následně vyjedná faxové parametry (jako datový tok a kompresi) s mobilní stanicí i se vzdáleným faxovým terminálem. Během fáze přenosu je entita T-FAX v síti zodpovědná za adaptaci signálů faxového modemu. Převádí signály modemu v audio pásmu z mobilní stanice (které jsou přenášeny přes rozhraní rádiového přístupu a páteřní sítě) do formátu vhodného pro přenos přes PSTN, která typicky používá 64 kbps [PCM](/mobilnisite/slovnik/pcm/) kanál (Pulse-Code Modulation) v [TDM](/mobilnisite/slovnik/tdm/) síti (Time-Division [Multiplexing](/mobilnisite/slovnik/multiplexing/)). To zahrnuje demodulaci, opravu chyb a případně adaptaci přenosové rychlosti.

S vývojem směrem k IP sítím, jako je IP Multimedia Subsystem (IMS), byl koncept T-FAX přizpůsoben. V IMS funkci T-FAX často ztělesňují Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) a Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) pro propojení s PSTN. Dále 3GPP definovala procedury pro "fax over IP", kde role T-FAX zahrnuje zpracování proudů protokolu [RTP](/mobilnisite/slovnik/rtp/) (Real-time Transport Protocol), které přenášejí signály faxového modemu jako audio pakety (s použitím kodeků jako G.711). Síť musí zajistit doručení těchto paketů s minimálním kolísáním zpoždění a ztrátou, aby byla zachována integrita faxové relace. Procedury T-FAX jsou podrobně popsány v 3GPP TS 23.146, která pokrývá technické realizace a scénáře propojení pro faxové služby napříč různými generacemi sítí.

## K čemu slouží

Technologie T-FAX byla standardizována za účelem podpory kritické starší služby – faksimilního přenosu – v nově vznikajících digitálních mobilních sítích. Když byl vyvíjen GSM, faxové přístroje byly dominantním nástrojem obchodní komunikace. Klíčovým požadavkem pro přijetí mobilních sítí podniky byla možnost odesílat a přijímat faxy z mobilních zařízení nebo prostřednictvím integrace pevné a mobilní sítě. Účelem definice T-FAX (a jeho protějšku R-FAX pro stranu příjmu) bylo vytvořit standardizovanou, spolehlivou metodu pro přenos signálů faxového modemu přes rádiovou a páteřní síť, které se zásadně liší od analogové PSTN.

Řešila problém degradace signálu a nekompatibility. Digitální kódování, komprese a potenciální chyby na rádiovém spoji mohly snadno narušit citlivé analogové navazování spojení a přenos dat faxového modemu během faxové relace. Procedury T-FAX zahrnují specifické režimy opravy chyb (jako ECM) a přesné algoritmy adaptace přenosové rychlosti, které tyto problémy zmírňují. Toto zajišťovalo, že fax odeslaný z mobilního telefonu měl stejnou spolehlivost a kvalitu jako fax odeslaný z tradiční pevné linky, což bylo zásadní pro přenos obchodních a právních dokumentů.

Jak se sítě vyvíjely směrem ke 3G, 4G a 5G, pokračující podpora T-FAX, byť jako volitelné funkce, byla hnána potřebou dlouhodobé kontinuity služeb. Některé vertikály, jako zdravotnictví, právní služby a námořní doprava, nadále spoléhaly na fax pro jeho jednoduchost, vnímanou bezpečnost a právní status. Standardizace T-FAX v IMS umožnila operátorům tuto službu zachovat při přechodu jejich páteřních sítí na plně IP architektury, což zajistilo, že mohou stále propojovat s rozsáhlou instalovanou základnou faxových přístrojů PSTN po celém světě.

## Klíčové vlastnosti

- Podpora protokolů faksimilního přenosu skupiny 3 ITU-T (Group 3) přes sítě 3GPP
- Funkce pro propojení mezi mobilními přenosovými službami (např. UDI, 3,1 kHz audio) a přenosem faxu přes PSTN
- Implementace adaptace signálů faxového modemu a adaptace přenosové rychlosti
- Podpora režimu opravy chyb (ECM) pro zajištění integrity dat přes spoje náchylné k chybám
- Procedury pro architektury sítí s přepojováním okruhů (CS) i pro IP Multimedia Subsystem (IMS)
- Řízení hovoru a vyjednávání přenosové služby specifické pro služby faksimilního přenosu

## Související pojmy

- [R-FAX – Reception Side Facsimile](/mobilnisite/slovnik/r-fax/)

## Definující specifikace

- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization

---

📖 **Anglický originál a plná specifikace:** [T-FAX na 3GPP Explorer](https://3gpp-explorer.com/glossary/t-fax/)
