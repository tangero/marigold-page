---
slug: "tmpi"
url: "/mobilnisite/slovnik/tmpi/"
type: "slovnik"
title: "TMPI – Temporary IP Multimedia Private Identity"
date: 2025-01-01
abbr: "TMPI"
fullName: "Temporary IP Multimedia Private Identity"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/tmpi/"
summary: "Dočasný identifikátor používaný v IMS k ochraně trvalé privátní identity uživatele (IMPI) před vystavením na rozhraní rádiového přenosu. Zvyšuje soukromí a bezpečnost účastníka během autentizačních a"
---

TMPI je dočasný identifikátor používaný v IMS k ochraně trvalé privátní identity uživatele před vystavením na rozhraní rádiového přenosu, čímž zvyšuje soukromí a bezpečnost během autentizace a registrace.

## Popis

Temporary IP Multimedia Private Identity (TMPI) je bezpečnostní mechanismus definovaný v architektuře IP Multimedia Subsystem (IMS) dle 3GPP. Jeho hlavní funkcí je ochránit trvalou IP Multimedia Private Identity ([IMPI](/mobilnisite/slovnik/impi/)) uživatele před přenosem v čitelné podobě nebo způsobem, který by mohl být odposlechnut na zranitelných síťových spojích, zejména na rádiovém rozhraní. TMPI je generován a přidělen sítí, konkrétně funkcí Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) nebo proxy uzlem, během procesu registrace v IMS. V následujících signalizačních zprávách, které procházejí nedůvěryhodnými cestami, slouží jako alias za IMPI, čímž brání dlouhodobému sledování a krádeži identity účastníka.

Operační tok zahrnuje počáteční registraci v IMS, kde se uživatelské zařízení (UE) autentizuje pomocí své trvalé IMPI. Po úspěšné autentizaci síť přidělí TMPI a bezpečně jej doručí UE, typicky v rámci chráněné odpovědi. Pro následné transakce v IMS, jako je opětovná registrace nebo zahájení relace, použije UE toto TMPI namísto IMPI v hlavičce P-Preferred-Identity nebo jiných relevantních polích [SIP](/mobilnisite/slovnik/sip/) při komunikaci s Proxy-CSCF ([P-CSCF](/mobilnisite/slovnik/p-cscf/)). Síťové uzly, které mají mapování mezi TMPI a skutečnou IMPI, mohou identitu interně rozpoznat pro servisní logiku a účtování. Tento mechanismus je klíčový ve scénářích, kdy referenční bod Gm mezi UE a P-CSCF není chráněn síťovou bezpečností jako [IPsec](/mobilnisite/slovnik/ipsec/), nebo v časných nasazeních IMS.

TMPI není samostatný přihlašovací údaj, ale funguje ve spojení s dalšími identitami a bezpečnostními asociacemi IMS. Liší se od Temporary Mobile Subscriber Identity ([TMSI](/mobilnisite/slovnik/tmsi/)) používané v jádrové síti s přepojováním okruhů a paketů, protože funguje na aplikační vrstvě pro služby založené na SIP. Správa TMPI zahrnuje jeho životnost, která je vázána na registrační relaci; TMPI se stává neplatným po vypršení registrace nebo při odregistrování. Použití TMPI je klíčovou funkcí pro ochranu soukromí požadovanou standardy 3GPP, která zajišťuje, že trvalá privátní identita účastníka není zbytečně vystavována, čímž se sladí s regulatorními požadavky na ochranu uživatelských dat.

## K čemu slouží

TMPI bylo zavedeno, aby řešilo významné problémy soukromí a bezpečnosti v časných nasazeních IMS. Trvalá IP Multimedia Private Identity ([IMPI](/mobilnisite/slovnik/impi/)), často strukturovaná jako Network Access Identifier ([NAI](/mobilnisite/slovnik/nai/)) (např. user@realm), je kritický dlouhodobý přihlašovací údaj. Přenos tohoto identifikátoru v čitelné podobě přes rádiové rozhraní, zejména před navázáním zabezpečených asociací, představoval velké riziko. Odposlouchávající strany mohly IMPI zachytit, což vedlo ke sledování a profilování účastníků a potenciálním útokům založeným na identitě. Motivací byla potřeba srovnat úroveň zabezpečení a ochrany soukromí v IMS s tou v doméně s přepojováním okruhů dle 3GPP, která již používala dočasné identifikátory jako TMSI.

Před zavedením TMPI mohla být IMPI vystavena v úvodních požadavcích SIP REGISTER nebo jiných zprávách, což vytvářelo mezeru v soukromí. Zatímco bezpečnostní mechanismy jako IMS Authentication and Key Agreement (AKA) a IPsec mohly chránit pozdější komunikaci, počáteční vystavení identity bylo slabinou. TMPI to řeší oddělením trvalé privátní identity od identifikátoru používaného v běžné signalizaci. Jeho vytvoření bylo hnací silou širšího bezpečnostního úkolu 3GPP 'IMS Privacy', který zajišťuje, že služby IMS neohrožují anonymitu uživatele. Řeší omezení spočívající pouze v zabezpečení přístupové sítě tím, že poskytuje ochranu soukromí na aplikační vrstvě, která je nezávislá na podkladovém transportu.

## Klíčové vlastnosti

- Chrání trvalou IMPI před vystavením na rádiovém rozhraní
- Je generován a přidělen sítí po úspěšné registraci v IMS
- Používá se v signalizaci SIP (např. v hlavičce P-Preferred-Identity) pro následné transakce
- Má životnost vázanou na registrační relaci v IMS
- Zvyšuje soukromí účastníka a snižuje riziko sledování
- Funguje na aplikační vrstvě v rámci bezpečnostní architektury IMS

## Související pojmy

- [IMPI – IP Multimedia CN subsystem Private Identity](/mobilnisite/slovnik/impi/)
- [IMPU – IP Multimedia Public User Identity](/mobilnisite/slovnik/impu/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)

## Definující specifikace

- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 33.220** (Rel-19) — Generic Authentication Architecture (GAA); Generic Bootstrapping Architecture (GBA)

---

📖 **Anglický originál a plná specifikace:** [TMPI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tmpi/)
