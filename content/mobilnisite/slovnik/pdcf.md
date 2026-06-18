---
slug: "pdcf"
url: "/mobilnisite/slovnik/pdcf/"
type: "slovnik"
title: "PDCF – Packetized DRM Content Format"
date: 2025-01-01
abbr: "PDCF"
fullName: "Packetized DRM Content Format"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pdcf/"
summary: "Formát specifikovaný 3GPP pro zapouzdření a doručování multimediálního obsahu chráněného systémem Digital Rights Management (DRM) přes paketově přepínané sítě. Definuje strukturovaný způsob balení šif"
---

PDCF je formát specifikovaný 3GPP pro zapouzdření a doručování multimediálního obsahu chráněného DRM přes paketově přepínané sítě. Umožňuje bezpečné distribuční služby, jako jsou stahování a streamování do mobilních zařízení.

## Popis

Packetized [DRM](/mobilnisite/slovnik/drm/) Content Format (PDCF) je technická specifikace definovaná 3GPP pro bezpečné doručování obsahu řízeného systémem Digital Rights Management (DRM). Nejde o DRM systém jako takový, ale o standardizovaný kontejnerový formát, který zapouzdřuje média chráněná DRM a jejich přidružená metadata. PDCF strukturovaně řadí obsah do logické sekvence paketů, z nichž každý obsahuje část šifrovaných mediálních dat (např. audio či video) a nezbytné informace pro jejich zpracování DRM agentem v klientském zařízení. Formát je navržen tak, aby byl nezávislý na přenosu, což umožňuje doručování přes různé IP-based přenašeče jako [HSPA](/mobilnisite/slovnik/hspa/), LTE nebo IMS.

Architektonicky se PDCF soubor nebo proud skládá z řady PDCF jednotek. Každá jednotka typicky obsahuje hlavičku a datovou část. Hlavička zahrnuje kritické řídicí informace, jako je identifikátor klíče pro šifrování obsahu, inicializační vektor pro dešifrování a pořadová čísla pro správné sestavení. Datová část obsahuje vlastní šifrovaná mediální data, často formátovaná podle specifického kodeku jako [AAC](/mobilnisite/slovnik/aac/) nebo H.264. Současně s mediálními pakety se doručují samostatné Rights Objects ([RO](/mobilnisite/slovnik/ro/)), které obsahují kryptografické klíče a pravidla užití (např. počet přehrání, datum vypršení platnosti) určující, jak lze obsah konzumovat. DRM agent na UE získává RO (obvykle ze serveru Rights Issuer) a používá ho k dešifrování a vynucení politik u média zabaleného v PDCF.

Jeho úloha v síti spočívá v umožnění bezpečných služeb doručování obsahu v rámci paketově přepínané ([PS](/mobilnisite/slovnik/ps/)) servisní architektury 3GPP. Funguje ve spojení se standardy DRM Open Mobile Alliance ([OMA](/mobilnisite/slovnik/oma/)) konsorcia 3GPP, konkrétně OMA DRM 2.0 a novějších verzí. Když poskytovatel služeb (např. mobilní hudební obchod) doručuje chráněný soubor, použije specifikaci PDCF k vytvoření balíčku ke stažení. Tento balíček je pak doručen přes standardní [HTTP](/mobilnisite/slovnik/http/) nebo [RTSP](/mobilnisite/slovnik/rtsp/) využívající IP konektivitu poskytovanou sítí 3GPP. Standardizovaný formát zajišťuje interoperabilitu mezi systémy pro přípravu obsahu od různých dodavatelů a DRM klientskými agenty na zařízeních od různých výrobců, čímž vytváří klíčový článek v koncovém hodnotovém řetězci komerčních mobilních mediálních služeb.

## K čemu slouží

PDCF byl vytvořen, aby vyřešil problém bezpečného, interoperabilního a efektivního doručování prémiového multimediálního obsahu přes paketově přepínané sítě 3GPP. Jak se mobilní sítě vyvíjely k podpoře vysokorychlostního přenosu dat (HSPA, LTE), operátoři a poskytovatelé obsahu usilovali o nabídku služeb, jako je stahování hudby a videí. Bez standardizovaného bezpečného kontejneru by však každý dodavatel DRM nebo poskytovatel služeb mohl používat proprietární metody balení, což by vedlo k fragmentaci, zvýšené složitosti zařízení (potřeba více klientských dekodérů) a vyšším nákladům na přípravu a distribuci obsahu.

Historický kontext představuje rozmach mobilních služeb obsahu v polovině roku 2000. 3GPP ve spolupráci s Open Mobile Alliance (OMA) vyvinula sadu standardů pro DRM. Zatímco OMA DRM definovala bezpečnostní a rights management protokoly, PDCF od 3GPP (specifikované v TS 26.234 a TS 26.247) definovalo samotný 'paketizovaný' formát pro šifrovaný obsah. Tím se vyřešila kritická mezera v tom, *jak* efektivně strukturovat šifrované bajty pro přenos po síti a zpracování na straně klienta, což umožnilo bezproblémový pracovní postup od šifrování obsahu přes jeho uložení až po přehrání na zařízení.

Dále PDCF řešilo omezení dřívějších, jednodušších metod DRM (jako forward-lock v OMA DRM 1.0), kterým chybělo sofistikované balení a nebyly vhodné pro obsah vysoké hodnoty. Poskytnutím standardizovaného formátu umožnil vývoj robustního ekosystému: poskytovatelé obsahu mohli kódovat jednou a distribuovat široce, výrobci mobilních zařízení mohli implementovat jediný, dobře specifikovaný klientský analyzátor a síťoví operátoři mohli nabízet standardizovanou doručovací platformu. To katalyzovalo růst komerčních trhů s mobilním obsahem snížením technických překážek a zajištěním konzistentního a bezpečného uživatelského zážitku pro placené multimediální služby.

## Klíčové vlastnosti

- Standardizovaný kontejner pro datové části médií chráněných DRM
- Strukturování obsahu do řazených PDCF jednotek s hlavičkami
- Nese identifikátory klíčů a inicializační vektory pro dešifrování
- Návrh nezávislý na přenosu pro doručování přes IP přenašeče
- Návrh pro interoperabilitu se systémy OMA DRM
- Podpora modelů doručování streamováním i stažením

## Související pojmy

- [PSS – Packet Switched Streaming Service](/mobilnisite/slovnik/pss/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP

---

📖 **Anglický originál a plná specifikace:** [PDCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdcf/)
