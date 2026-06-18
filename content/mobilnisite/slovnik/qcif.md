---
slug: "qcif"
url: "/mobilnisite/slovnik/qcif/"
type: "slovnik"
title: "QCIF – Quarter Common Intermediate Format"
date: 2025-01-01
abbr: "QCIF"
fullName: "Quarter Common Intermediate Format"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/qcif/"
summary: "Standardizovaný formát video rozlišení o rozměrech 176x144 pixelů. Představuje jednu čtvrtinu rozlišení Common Intermediate Format (CIF). Primárně používán v rané 3GPP video telefonii a službách multi"
---

QCIF je standardizovaný formát video rozlišení 176x144 pixelů, představující jednu čtvrtinu rozlišení CIF, používaný v rané 3GPP video telefonii a MMS pro mobilní sítě s nízkou přenosovou rychlostí.

## Popis

Quarter Common Intermediate Format (QCIF) je standard video rozlišení definovaný v doporučení [ITU-T](/mobilnisite/slovnik/itu-t/) H.261 a přijatý v rámci 3GPP pro multimediální služby. Jeho prostorové rozlišení je 176 pixelů horizontálně a 144 pixelů vertikálně, což je přesně jedna čtvrtina plochy Common Intermediate Format ([CIF](/mobilnisite/slovnik/cif/), 352x288). Formát používá schéma chrominance subsamplingu 4:2:0, což znamená, že informace o barvě (chrominance) je vzorkována v polovičním rozlišení jak horizontálně, tak vertikálně ve srovnání s informací o jasu (luminance). Tím se sníží nezpracovaná datová rychlost bez výrazného vnímaného zhoršení kvality barev, což je klíčový faktor pro mobilní sítě s omezenou přenosovou rychlostí.

V kontextu 3GPP byl QCIF specifikován jako povinné rozlišení video kodeku pro okruhově spínanou 3G-324M video telefonii a pro paketově spínanou službu multimediálních zpráv ([MMS](/mobilnisite/slovnik/mms/)). Protokolový zásobník 3G-324M, používaný přes okruhově spínané přenosové kanály UMTS, vyžadoval podporu video kodeku H.263 v rozlišení QCIF (15 snímků za sekundu), aby byla zajištěna základní interoperabilita mezi zařízeními a sítěmi různých výrobců. Pro MMS specifikace 3GPP definovaly mediální profily, které zahrnovaly QCIF jako cílové rozlišení pro video klipy, aby bylo zajištěno, že zprávy zůstanou v rámci velikostních limitů a mohou být zobrazeny na široké škále zařízení s omezenými možnostmi displeje a výpočetním výkonem.

Technická implementace zahrnuje video kodeky jako H.263, MPEG-4 Part 2 nebo pozdější H.264/[AVC](/mobilnisite/slovnik/avc/), které kódují a dekódují video snímky v rozlišení QCIF. Role sítě byla primárně poskytovat přenosovou službu (buď okruhově spínaný 64 kbps kanál nebo paketově spínané datové připojení) schopnou přenášet zakódovaný bitový proud. Specifikace, jako například TS 26.234 pro paketově spínané streamování, podrobně popisují formáty [RTP](/mobilnisite/slovnik/rtp/) payload a protokoly pro popis relace používané k vyjednání a doručení QCIF video obsahu. Ačkoli byl v moderních smartphonech z velké části nahrazen vyššími rozlišeními, QCIF představoval klíčový mezistupeň při umožnění reálné video komunikace na raných 3G mobilních zařízeních.

## K čemu slouží

QCIF byl přijat za účelem umožnění praktických služeb video komunikace na omezené přenosové rychlosti a výpočetním výkonu sítí 2.5G a raných 3G. Před rozšířením mobilního videa neexistoval standardizovaný formát nízkého rozlišení, který by mohl garantovat interoperabilitu mezi různým síťovým zařízením a výrobci mobilních zařízení. Vytvoření jednoduché, čtvrtinové verze [CIF](/mobilnisite/slovnik/cif/) poskytlo zvládnutelný cíl pro návrháře kodeků a výrobce zařízení, což zajišťovalo, že video telefonické hovory mohou být úspěšně navázány mezi jakýmikoli kompatibilními zařízeními.

Řešil základní problém vměstnání reálného video proudu do velmi omezených datových kanálů (např. jediného 64 kbps časového slotu v UMTS). Vyšší rozlišení jako CIF nebo [VGA](/mobilnisite/slovnik/vga/) by vyžadovala větší přenosovou rychlost, než byla ekonomicky dostupná, nebo by vedla k nepřijatelně nízké snímkové frekvenci nebo vysokým kompresním artefaktům. Standardizací QCIF jako povinné základní úrovně zajistilo 3GPP minimální životaschopný uživatelský zážitek z video hovorů a umožnilo multimediální zasílání zpráv, což pohánělo adopci těchto nových služeb. Řešilo omezení čistě proprietárních řešení a bylo klíčovým umožňovatelem první vlny mobilních video aplikací.

## Klíčové vlastnosti

- Standardizované rozlišení 176x144 pixelů (1/4 CIF)
- Povinná podpora pro okruhově spínanou 3G-324M video telefonii
- Použití chrominance subsamplingu 4:2:0 ke snížení přenosové rychlosti
- Cílové rozlišení pro video klipy v rané službě multimediálních zpráv (MMS)
- Umožnění interoperability mezi zařízeními a sítěmi různých výrobců
- Optimalizováno pro nízkobitové kódování s kodeky jako H.263 a MPEG-4

## Související pojmy

- [CIF – Common Intermediate Format](/mobilnisite/slovnik/cif/)
- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)

## Definující specifikace

- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization

---

📖 **Anglický originál a plná specifikace:** [QCIF na 3GPP Explorer](https://3gpp-explorer.com/glossary/qcif/)
