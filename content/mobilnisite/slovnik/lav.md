---
slug: "lav"
url: "/mobilnisite/slovnik/lav/"
type: "slovnik"
title: "LAV – Least Acceptable Value"
date: 2025-01-01
abbr: "LAV"
fullName: "Least Acceptable Value"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lav/"
summary: "Parametr QoS definující minimální přijatelnou hodnotu pro konkrétní výkonnostní metrikum, jako je propustnost nebo zpoždění. Používá se při výběru sítě a rozhodování o politikách k zajištění, že uživa"
---

LAV je parametr QoS definující minimální přijatelnou hodnotu výkonnostního metriku, používaný při výběru sítě k zajištění, že uživatelský zážitek splňuje základní práh.

## Popis

Least Acceptable Value (LAV) je parametr kvality služby (QoS) standardizovaný ve specifikacích 3GPP, primárně v kontextu výběru sítě, řízení politik a kontinuity služby. Představuje dolní mez nebo práh pro konkrétní výkonnostní metrikum, který musí být splněn, aby byla síť nebo přenosový kanál považována za přijatelnou pro danou službu nebo aplikaci. LAV není jediná univerzální hodnota, ale je definována pro každý metrikum zvlášť, například Guaranteed Bit Rate ([GBR](/mobilnisite/slovnik/gbr/)), Packet Delay Budget (PDB) nebo Packet Error Loss Rate (PELR). Funguje jako smluvní minimum; pokud síť tuto hodnotu nemůže garantovat, služba může být zamítnuta, předána jinam nebo uživatel může zaznamenat sníženou kvalitu.

Z architektonického hlediska jsou parametry LAV typicky komunikovány a vynucovány v rámci core sítě za účasti prvků jako Policy and Charging Rules Function (PCRF) nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G. Během zřizování nebo modifikace session může User Equipment (UE) nebo aplikační server indikovat své požadavky na LAV. Rámec pro řízení politik v síti je pak vyhodnotí vůči dostupným zdrojům a aktuálním podmínkám. Pokud se síť nemůže zavázat ke splnění LAV, může odmítnout žádost o zřízení přenosového kanálu, spustit vyhledání alternativní přístupové sítě (např. prostřednictvím politik [ANDSF](/mobilnisite/slovnik/andsf/)) nebo aplikovat alternativní QoS profily.

V provozu LAV spolupracuje s dalšími parametry QoS, jako je Maximum Allowed Value nebo požadované hodnoty, a vytváří tak rozsah přijatelnosti. Například služba streamování videa může mít LAV pro downlink GBR, aby se zabránilo bufferingu, a zároveň může mít požadovanou vyšší rychlost pro optimální kvalitu. Síť používá LAV pro řízení přístupu (admission control) a rezervaci zdrojů. Zajišťuje, že přijaté session mají vysokou pravděpodobnost obdržení svých minimálně požadovaných zdrojů, čímž chrání QoS existujících session a udržuje celkovou stabilitu sítě. To je odlišné, ale komplementární k parametrům jako Aggregate Maximum Bit Rate ([AMBR](/mobilnisite/slovnik/ambr/)), které řídí sdílení, zatímco LAV definuje minimální úroveň na session.

Role LAV je klíčová v prostředích s více přístupy a heterogenních sítích. S technologiemi jako LTE-WLAN Aggregation ([LWA](/mobilnisite/slovnik/lwa/)) nebo 5G Non-Standalone (NSA) architektury pomáhá LAV při přijímání inteligentních rozhodnutí o směrování provozu. Pokud výkon primárního přístupového spoje klesne pod LAV pro přenosový kanál, síť může iniciovat handover nebo přesměrovat provoz na sekundární cestu. Je také relevantní pro network slicing, kde musí instance slicu garantovat určité minimální výkonnostní úrovně jako součást své Service Level Agreement (SLA). LAV je tedy základním stavebním kamenem pro zajištění předvídatelné a spolehlivé QoS v moderních celulárních sítích.

## K čemu slouží

Koncept Least Acceptable Value byl zaveden, aby řešil rostoucí potřebu detailnějších a vynutitelných QoS garancí v paketově přepínaných celulárních sítích. Rané služby mobilních dat (např. [GPRS](/mobilnisite/slovnik/gprs/), rané [HSPA](/mobilnisite/slovnik/hspa/)) nabízely best-effort připojení s omezenou diferenciací QoS. Jak se služby vyvíjely a zahrnovaly aplikace v reálném čase, jako je Voice over IP (VoIP), streamování videa a online hry, pouhé poskytování 'best effort' se stalo nedostatečným. Tyto aplikace mají striktní minimální požadavky na latenci, kolísání zpoždění (jitter) a propustnost, aby fungovaly přijatelně. Bez definovaného minimálního prahu mohly sítě přijímat provoz, který by nevyhnutelně selhal, což plýtvalo zdroji a degradovalo uživatelský zážitek.

LAV to řeší tím, že poskytuje jasnou, vyjednatelnou dolní mez pro kvalitu služby. Umožňuje síti provádět smysluplné řízení přístupu (admission control). Než síť přidělí zdroje novému přenosovému kanálu nebo session, může zkontrolovat, zda dokáže udržitelně poskytnout LAV. Tím se zabrání nadměrnému přijímání provozu a kongescím, kdy je přijato příliš mnoho náročných session, což způsobí, že všechny nesplní své požadavky. Posouvá správu QoS z reaktivního, měřením založeného přístupu k více prediktivnímu modelu založenému na rezervaci zdrojů. To je obzvláště důležité pro přenosové kanály s garantovanou přenosovou rychlostí ([GBR](/mobilnisite/slovnik/gbr/) bearers), které se používají pro konverzační hlas a živé video.

LAV navíc usnadňuje kontinuitu služby a mobilitu v heterogenních sítích. Když se uživatelé pohybují mezi buňkami nebo přepínají mezi 3GPP a non-3GPP přístupem (jako Wi-Fi), potřebuje síť kritéria pro rozhodování, kdy je handover nezbytný z důvodu QoS. Pokles výkonu pod LAV slouží jako konkrétní spouštěč. Umožňuje také uživatelskému zařízení a aplikacím explicitně vyjádřit své minimální potřeby, což umožňuje inteligentnější politiky výběru sítě. LAV v podstatě formalizuje koncept 'minimální úrovně služby', což je předpoklad pro poskytování spolehlivých, operátorské kvality služeb přes IP-based mobilní sítě.

## Klíčové vlastnosti

- Definuje minimální QoS práh pro každý metrikum (např. pro GBR, zpoždění, ztrátu).
- Používá se jako kritérium pro řízení přístupu do sítě (admission control) a zřizování přenosových kanálů.
- Spouští síťově iniciované handovery nebo přesměrování provozu při porušení.
- Komunikuje se mezi UE, sítí a funkcemi pro řízení politik (např. PCRF, PCF).
- Nedílná součást mechanismů vynucování QoS politik a rezervace zdrojů.
- Podporuje kontinuitu služby v prostředích s více RAT a heterogenních sítích.

## Definující specifikace

- **TR 26.944** (Rel-19) — QoE, ESQoS and SQoS metrics for 3G multimedia services

---

📖 **Anglický originál a plná specifikace:** [LAV na 3GPP Explorer](https://3gpp-explorer.com/glossary/lav/)
