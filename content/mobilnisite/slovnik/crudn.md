---
slug: "crudn"
url: "/mobilnisite/slovnik/crudn/"
type: "slovnik"
title: "CRUDN – Create, Retrieve, Update, Delete and Notify"
date: 2026-01-01
abbr: "CRUDN"
fullName: "Create, Retrieve, Update, Delete and Notify"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/crudn/"
summary: "CRUDN je standardizovaná sada operací správy dat definovaná organizací 3GPP pro Service Enabler Architecture Layer (SEAL). Poskytuje společný rámec API pro vytváření, čtení, aktualizaci, mazání a odeb"
---

CRUDN je standardizovaná sada operací správy dat v architektuře SEAL organizace 3GPP, která poskytuje společné API pro vytváření, získávání, aktualizaci, mazání a odebírání notifikací pro síťové datové objekty.

## Popis

CRUDN představuje základní sadu operací správy dat standardizovaných v rámci architektury Service Enabler Architecture Layer ([SEAL](/mobilnisite/slovnik/seal/)) organizace 3GPP, jak je specifikováno v TS 23.434. Tyto operace tvoří základní [API](/mobilnisite/slovnik/api/) prvky pro správu datových objektů v síťových repozitářích a služebních enablerech. Rámec definuje standardizované formáty požadavků a odpovědí, postupy zpracování chyb a modely reprezentace dat, které zajišťují interoperabilitu mezi různými komponentami služeb a aplikacemi.

Architektonicky jsou operace CRUDN implementovány prostřednictvím RESTful API nebo jiných standardizovaných rozhraní, která zpřístupňují možnosti správy dat autorizovaným klientům. Operace Create umožňuje klientům vytvořit nové datové objekty s konkrétními atributy a identifikátory v datovém repozitáři. Retrieve umožňuje dotazování a čtení existujících datových objektů a podporuje jak získání jednotlivých objektů, tak hromadné dotazy s možnostmi filtrování. Update poskytuje mechanismy pro úpravu existujících datových objektů, včetně částečných aktualizací a úplných nahrazení atributů objektu.

Operace Delete odstraňují datové objekty z repozitáře s konfigurovatelnými politikami kaskádového mazání pro související objekty. Operace Notify zavádí mechanismy předplatného, kde si klienti mohou zaregistrovat asynchronní notifikace při změně stavu konkrétních datových objektů nebo při výskytu určitých událostí. Tento vzor publish-subscribe umožňuje efektivní architektury řízené událostmi bez nutnosti průběžného dotazování. Rámec zahrnuje komplexní bezpečnostní mechanismy včetně autentizace, autorizace a ochrany dat pro všechny operace.

CRUDN funguje v rámci širší architektury SEAL, která poskytuje společné služební enablery pro vertikální aplikace. Datové objekty spravované prostřednictvím operací CRUDN zahrnují uživatelské profily, konfigurace služeb, pravidla politik, stavy relací a data specifická pro aplikace. Operace podporují verzování, řízení souběžnosti prostřednictvím optimistického zamykání a transakční konzistenci tam, kde je to vyžadováno. Mezi optimalizace výkonu patří strategie ukládání do mezipaměti, dávkové operace a efektivní mechanismy doručování notifikací, které minimalizují síťovou režii při zachování konzistence dat v distribuovaných systémech.

## K čemu slouží

CRUDN byl zaveden, aby řešil roztříštěnost rozhraní pro správu dat napříč různými služebními enablery 3GPP a vertikálními aplikacemi. Před jeho standardizací implementoval každý služební komponent proprietární rozhraní pro správu dat s odlišnou sémantikou [API](/mobilnisite/slovnik/api/), zpracováním chyb a bezpečnostními modely. To vytvářelo značnou integrační složitost pro vývojáře aplikací a síťové operátory, kteří potřebovali komunikovat s více síťovými funkcemi.

Primárním motivem bylo vytvořit společný, znovupoužitelný vzor pro operace správy dat, který by mohl být konzistentně aplikován napříč architekturou služeb 3GPP. Standardizací těchto základních operací chtěla organizace 3GPP snížit vývojové úsilí, zlepšit interoperabilitu a umožnit rychlejší nasazení nových služeb. Rámec zvláště podporuje potřeby vertikálních odvětví (jako je automobilový průmysl, průmyslový IoT a média), která vyžadují konzistentní možnosti správy dat napříč různými síťovými řezy a služebními enablery.

CRUDN řeší problém nekonzistentních přístupových vzorů k datům tím, že poskytuje jednotný přístup fungující napříč různými datovými repozitáři a služebními komponentami. Umožňuje vývojářům aplikací používat známé vzory bez ohledu na podkladovou síťovou funkci a zároveň dává síťovým operátorům konzistentní kontrolu nad politikami přístupu k datům a bezpečností. Mechanismus notifikací konkrétně řeší výzvu synchronizace dat v reálném čase v distribuovaných systémech a odstraňuje potřebu neefektivních mechanismů dotazování, které plýtvají síťovými prostředky.

## Klíčové vlastnosti

- Standardizované operace RESTful API pro správu dat
- Komplexní bezpečnostní rámec zahrnující autentizaci a autorizaci
- Systém notifikací řízený událostmi se správou předplatného
- Podpora hromadných operací a filtrování dotazů
- Mechanismy verzování a optimistického řízení souběžnosti
- Interoperabilita napříč různými služebními enablery SEAL

## Související pojmy

- [SEAL – Service Enabler Architecture Layer for Verticals](/mobilnisite/slovnik/seal/)
- [CAPIF – Common API Framework](/mobilnisite/slovnik/capif/)

## Definující specifikace

- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals

---

📖 **Anglický originál a plná specifikace:** [CRUDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/crudn/)
