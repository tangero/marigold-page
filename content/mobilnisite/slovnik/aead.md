---
slug: "aead"
url: "/mobilnisite/slovnik/aead/"
type: "slovnik"
title: "AEAD – Authenticated Encryption with Associated Data"
date: 2026-01-01
abbr: "AEAD"
fullName: "Authenticated Encryption with Associated Data"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/aead/"
summary: "AEAD je kryptografický primitiv, který v systémech 3GPP současně poskytuje důvěrnost, integritu a autenticitu dat. Šifruje užitečná data a zároveň generuje autentizační značku jak pro šifrový text, ta"
---

AEAD je kryptografická metoda, která současně zajišťuje důvěrnost, integritu a autenticitu tím, že zašifruje užitečná data a vygeneruje autentizační značku jak pro šifrový text, tak pro jakákoliv přidružená nešifrovaná data.

## Popis

Authenticated Encryption with Associated Data (AEAD) je operace symetrické kryptografie, která kombinuje šifrování a autentizaci do jediného zabezpečeného režimu. V systémech 3GPP je specifikována jako primární mechanismus pro ochranu provozu v uživatelské a řídicí rovině, zejména v rámci bezpečnostní architektury 5G definované v TS 33.501. Základní funkce přijímá čtyři vstupy: tajný klíč, jednorázové číslo (nonce), otevřenou zprávu určenou k zašifrování a přidružená data (Associated Data, AD), která vyžadují autentizaci, nikoliv však šifrování. Produkuje dva výstupy: šifrový text (zašifrovanou verzi otevřené zprávy) a autentizační značku.

Algoritmus funguje tak, že zpracovává jak otevřenou zprávu, tak přidružená data prostřednictvím kryptografické konstrukce, která poskytuje nerozlišitelnost při útocích s volbou otevřeného textu (IND-CPA) pro důvěrnost a existenční nepadělatelnost při útocích s volbou zprávy (EUF-CMA) pro integritu. Přidružená data, která mohou zahrnovat hlavičky paketů, sekvenční čísla nebo jiná metadata klíčová pro funkci protokolu, jsou autentizována, ale přenášena v čitelné podobě. To umožňuje mezilehlým síťovým uzlům (jako jsou gNB nebo [UPF](/mobilnisite/slovnik/upf/)) kontrolovat potřebné informace v hlavičkách bez narušení zabezpečení zašifrovaných užitečných dat.

V implementacích 3GPP jsou povinné konkrétní AEAD algoritmy, jako je AES-GCM (Galois/Counter Mode) a ChaCha20-Poly1305. Pro 5G je primárním algoritmem pro ochranu signalizace [NAS](/mobilnisite/slovnik/nas/) a [RRC](/mobilnisite/slovnik/rrc/) a také pro ochranu integrity uživatelské roviny (pokud je povolena) 128bitový AES-GCM. Jednorázové číslo (nonce) musí být pro každé volání se stejným klíčem jedinečné a typicky se konstruuje z parametrů jako hodnota COUNT (pro signalizaci) nebo PDCP SN a identita přenosového kanálu (pro uživatelskou rovinu). Délka autentizační značky je u AES-GCM typicky 16 bajtů (128 bitů), což poskytuje vysokou míru jistoty proti pokusům o padělání.

Úloha AEAD v síti je všudypřítomná. Zajišťuje zabezpečení rozhraní N1 (UE-AMF) a [N2](/mobilnisite/slovnik/n2/) (RAN-AMF) pro signalizaci v řídicí rovině. Pro uživatelskou rovinu může poskytovat jak důvěrnost, tak ochranu integrity (podle indikace 'integrity protected') na rozhraních Uu (UE-gNB) a N3 (gNB-UPF). Jeho efektivita – vyžadující pouze jediný průchod daty pro šifrování i autentizaci – snižuje latenci a výpočetní režii ve srovnání s použitím samostatných šifrovacích a [MAC](/mobilnisite/slovnik/mac/) algoritmů, což je klíčové pro vysokopropustné aplikace 5G.

## K čemu slouží

AEAD byl zaveden, aby odstranil omezení předchozích bezpečnostních mechanismů 3GPP, které často používaly samostatné, kompoziční přístupy pro šifrování a integritu. Ve 4G (EPS) poskytovaly důvěrnost a integritu odlišné algoritmy (např. SNOW 3G nebo [AES](/mobilnisite/slovnik/aes/) pro šifrování a samostatný [MAC](/mobilnisite/slovnik/mac/) pro integritu). Tento kompoziční přístup, ačkoliv bezpečný při správné implementaci, je složitější, méně efektivní a náchylný k implementačním chybám. Přechod na AEAD v 5G je v souladu s moderními osvědčenými postupy v kryptografii, zjednodušuje návrh protokolů a snižuje prostor pro možné útoky.

Hlavní motivací bylo zvýšit bezpečnostní záruky a výkon pro rozmanité požadavky služeb 5G, včetně rozšířeného mobilního širokopásmového připojení (eMBB), ultra-spolehlivé komunikace s nízkou latencí (URLLC) a hromadného internetu věcí (IoT). AEAD algoritmy jsou prokazatelně bezpečné za standardních předpokladů a nabízejí robustní ochranu proti pasivnímu odposlechu i aktivnímu narušování. Jejich jednoprůchodová povaha je klíčová pro dosažení cílů nízké latence služeb URLLC a pro zvládání vysokých přenosových rychlostí eMBB bez zavádění významných zpracovatelských zpoždění.

Navíc AEAD podporuje autentizaci přidružených dat, což je pro protokoly 3GPP nezbytné. Hlavičky paketů, sekvenční čísla a identifikátory QoS toků často potřebují být autentizovány, aby se zabránilo útokům na úrovni protokolu (jako je opakování nebo změna pořadí), ale nevyžadují šifrování pro funkčnost sítě. AEAD to elegantně řeší tím, že umožňuje zahrnout tato metadata do autentizačního výpočtu bez jejich zašifrování, což umožňuje efektivní provoz sítě při zachování silné bezpečnostní záruky.

## Klíčové vlastnosti

- Současná ochrana důvěrnosti a integrity v jediné kryptografické operaci
- Autentizace přidružených dat (AD), která zůstávají v čitelné podobě
- Použití prokazatelně bezpečných algoritmů, jako je AES-GCM, dle specifikace 3GPP
- Povinná podpora 128bitového AES-GCM ve všech bezpečnostních profilech 5G
- Jedinečná konstrukce jednorázového čísla (nonce) z parametrů protokolu (např. COUNT, PDCP SN) k zabránění opakovaného použití
- Jednoprůchodové zpracování pro nízkou latenci a vysokou efektivitu vhodnou pro propustnost 5G

## Definující specifikace

- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G

---

📖 **Anglický originál a plná specifikace:** [AEAD na 3GPP Explorer](https://3gpp-explorer.com/glossary/aead/)
