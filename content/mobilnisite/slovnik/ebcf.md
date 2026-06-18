---
slug: "ebcf"
url: "/mobilnisite/slovnik/ebcf/"
type: "slovnik"
title: "EBCF – Event Based Charging Function"
date: 2025-01-01
abbr: "EBCF"
fullName: "Event Based Charging Function"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ebcf/"
summary: "Základní funkce Online Charging Systemu (OCS), která provádí účtování v reálném čase na základě konkrétních událostí v síti nebo službě, nikoli pouze podle délky trvání nebo objemu dat. Umožňuje flexi"
---

EBCF je funkce Online Charging Systemu, která provádí účtování v reálném čase na základě konkrétních událostí v síti nebo službě, aby umožnila flexibilní, kontextově citlivé účtování pro komplexní služby.

## Popis

Event Based Charging Function (EBCF) je základní komponenta v rámci 3GPP Online Charging Systemu ([OCS](/mobilnisite/slovnik/ocs/)). Jejím úkolem je provádět účtovací logiku v reálném čase pro události služeb. Na rozdíl od účtování založeného na relaci nebo objemu dat, které je kontinuální, je účtování založené na událostech spouštěno diskrétními případy. EBCF přijímá účtovací události od síťových funkcí, jako je Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN), Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) nebo IMS Call Session Control Functions (CSCFs), prostřednictvím referenčních bodů Ro nebo Gy. Tyto události nesou informace, jako je identita účastníka, typ události a relevantní parametry služby.

Architektonicky se EBCF nachází v rámci OCS a spolupracuje s funkcí správy zůstatku na účtu (Account Balance Management Function – [ABMF](/mobilnisite/slovnik/abmf/)) a Rating Function ([RF](/mobilnisite/slovnik/rf/)). Když dorazí požadavek na účtování, EBCF jej zpracuje. Nejprve provede identifikaci účastníka a získá relevantní informace o účtu a účtovací pravidla z ABMF. Poté použije RF k určení peněžní nebo nepeněžní ceny (v jednotkách, jako jsou kredity) spojené s konkrétní událostí. Toto ocenění může být složité a záviset na faktorech, jako je typ události, typ služby, umístění, denní doba a úroveň předplatitele. Po ocenění EBCF instruuje ABMF, aby v reálném čase odečetla příslušnou částku ze zůstatku účastníka.

Jak to funguje, je založeno na politice a autorizaci v reálném čase. Pro každou událost musí EBCF učinit okamžité rozhodnutí: událost autorizovat (pokud existuje dostatečný zůstatek), nebo ji zamítnout. Například když uživatel odešle [MMS](/mobilnisite/slovnik/mms/), MMS server odešle účtovací událost do OCS. EBCF ocení tuto událost typu 'odeslání MMS', zkontroluje zůstatek a pokud ji autorizuje, umožní odeslání MMS a současně odečte cenu. Poté vrátí odpověď síťovému prvku. EBCF podporuje různé typy událostí, včetně událostí služby (např. stažení obsahu, [SMS](/mobilnisite/slovnik/sms/), MMS), událostí konfigurace služby (např. aktivace pravidla přesměrování hovoru) a událostí správy (např. doplnění zůstatku). Generuje záznamy o účtovacích datech (Charging Data Records – CDRs) pro účely fakturace a auditu.

## K čemu slouží

EBCF byla vytvořena, aby řešila omezení tradičních, zjednodušených účtovacích modelů založených pouze na délce hovoru nebo počtu megabajtů. Jak se mobilní sítě vyvíjely a nabízely širokou škálu služeb mimo hlas – jako jsou zprávy ([SMS](/mobilnisite/slovnik/sms/)/MMS), stahování obsahu, služby založené na poloze a funkce IMS – potřebovali operátoři flexibilní způsob účtování těchto diskrétních, nekontinuálních transakcí. Paušální sazba za data nebo poplatek za hlasovou minutu nemohly zachytit hodnotu nebo strukturu nákladů na odeslání MMS nebo přístup k prémiové úrovni hry. EBCF poskytuje mechanismus pro toto detailní, službám přizpůsobené účtování.

Zavedená ve vydání 8 jako součást vylepšené architektury OCS, EBCF vyřešila problém řízení kreditu v reálném čase pro služby založené na událostech. Umožnila předplacené nabídky pro služby nezávislé na relaci, což byla hlavní obchodní potřeba. Bez ní by se operátoři museli spoléhat na méně přesné offline účtování nebo by museli všechny služby nutit do modelů založených na relaci. EBCF umožňuje operátorům definovat sofistikované tarifní plány, které účtují různé částky za různé typy událostí, což podporuje inovace služeb a personalizované ceny. Je klíčovým prvkem pro monetizaci rozsáhlého ekosystému služeb v moderních mobilních sítích.

## Klíčové vlastnosti

- Provádí řízení kreditu v reálném čase pro diskrétní události služeb
- Komunikuje se síťovými prvky prostřednictvím referenčních bodů Ro (pro IMS/aplikace) a Gy (pro data)
- Integruje se s Rating Function pro výpočet ceny a s Account Balance Management Function pro aktualizace zůstatku
- Podporuje operace autorizace, odečtu a vrácení prostředků pro události
- Zpracovává různé typy událostí: využití služby, konfigurace služby a správa zůstatku
- Generuje záznamy o účtování událostí (Event Charging Data Records – ECDRs) pro fakturaci

## Definující specifikace

- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification
- **TS 32.296** (Rel-19) — Online Charging System (OCS) Architecture
- **TS 32.825** (Rel-10) — Study on Rc Reference Point for ABMF

---

📖 **Anglický originál a plná specifikace:** [EBCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ebcf/)
